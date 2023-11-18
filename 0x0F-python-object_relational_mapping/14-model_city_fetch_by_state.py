#!/usr/bin/python3
"""
Prints all city objects in database
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State
from model_city import City
from sys import argv

if __name__ == "__main__":

    Base = declarative_base()
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).join(State).order_by(City.id)

    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")
