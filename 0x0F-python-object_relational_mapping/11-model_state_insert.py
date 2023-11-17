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
    if session:
        new_state = State()
        new_state.name = "Louisiana"
        session.add(new_state)
        session.commit()
        print(new_state.id)
