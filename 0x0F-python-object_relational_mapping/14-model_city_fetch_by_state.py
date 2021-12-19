#!/usr/bin/python3
""" print all City objects from the database"""
if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()
    for c, s in session.query(City, State).select_from(State).join(City).all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
