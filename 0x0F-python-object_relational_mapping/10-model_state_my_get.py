#!/usr/bin/python3
""" print id of a state given"""
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
    try:
        state = session.query(State)\
            .filter(State.name == argv[4]).order_by(State.id).all()[0]
        print(state.id)
    except IndexError:
        print("Not found")
    session.close()
