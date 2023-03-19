#!/usr/bin/python3
"""
Contains the class definition of a City and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Class representing the cities table
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    states.id = Column(Integer, ForeignKey('states.id'), nullable=False)
