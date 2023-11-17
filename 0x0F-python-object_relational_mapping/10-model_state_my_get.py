#!/usr/bin/python3
"""
that prints the State object with the name passed as argument
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
                State.name == argv[4])

    if (states.count() == 0):
        print("Not found")
    else:
        for state in states:
            print(f"{state.id}")
