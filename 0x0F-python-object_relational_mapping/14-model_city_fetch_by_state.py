#!/usr/bin/python3
"""
Prints all city objects in database
"""


import sys
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City


if (__name__ == "__main__"):

    usrname = sys.argv[1]
    passwrd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(usrname,
                                   passwrd,
                                   db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    result = session.query(State, City).join(City).order_by(City.id)
    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
