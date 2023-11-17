#!/usr/bin/python3
"""
Fetch all States from the given database.
"""


from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine


if (__name__ == '__main__'):
    engine = create_engine(f"mysql:///{argv[3]}", pool_per_ping=True)

    Session = sessionmaker(engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
