#!/usr/bin/python3
"""First state model"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class State"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)

    def __str__(self):
        """formato a mostrar al print (instance)"""
        return f"{self.id}: {self.name}"
