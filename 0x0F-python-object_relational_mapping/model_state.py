#!/usr/bin/python3

"""
    class definition
"""

from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        table state
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, auto_increment=True)
    name = Column(Text(128), nullable=False)
