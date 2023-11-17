#!/usr/bin/python3
"""
Fetch all States from the given database.
"""


from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine


if (__name__ == '__main__'):
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost\
        :3306/{argv[3]}", pool_pre_ping=True)

    Session = sessionmaker(engine)
    with Session() as session:
        states = session.query(State)

        for state in states:
            print(f"{state.id}: {state.name}")
