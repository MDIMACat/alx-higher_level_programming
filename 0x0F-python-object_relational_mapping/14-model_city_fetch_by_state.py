#!/usr/bin/python3
"""
Prints all city objects in database
"""


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import Base, City
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id)
    for city in cities:
        print("{}: ({}) {}".format(State.name, City.id, City.name))
