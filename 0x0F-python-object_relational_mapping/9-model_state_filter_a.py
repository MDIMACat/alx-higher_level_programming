#!/usr/bin/python3
"""
Fetch all States from the given database.
"""


from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(
                State.name.contains("a"))

    for state in states:
        print("{}: {}".format(state.id, state.name))
