#!/usr/bin/python3
"""
Creates the cities Table in the database
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """City class used to create a cities table in 
    database
    """
    
    __tablename__ = 'cities'
    
    id = Column('id',Integer,primary_key=True, autoincrement=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'), nullable=False)
    states = relationship('State')

