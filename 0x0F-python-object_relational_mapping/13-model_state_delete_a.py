#!/usr/bin/python3
""" delete all State objects with a name containing the letter a"""
if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()
    for obj in session.query(State).filter(State.name.like('%a%')):
        session.delete(obj)
    session.commit()
    session.close()
