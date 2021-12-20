#!/usr/bin/python3
""" list all State objects from the database hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':

    """ Initialize the database :: Connection & Metadata retrieval"""
    
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    """ SqlAlchemy :: factory of sessions bound to the engine object created earlier"""
    
    Session = sessionmaker(bind=engine)

""" Create all tables that do not already exist"""
    Base.metadata.create_all(engine)

""" SqlAlchemy :: Starts a session (session object)"""
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
