#!/usr/bin/python3
"""Definir una nueva clase City - similar State"""
"""Modelando una nueva tabla cities"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Class city que hereda de Base"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = (Integer, nullable=False, ForeignKey("states.id"))
