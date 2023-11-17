#!/usr/bin/python3
"""
Defines a class that maps to a database
table called states.
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State class in database"""
    __tablename__ = 'State'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
