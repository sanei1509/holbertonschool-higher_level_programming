#!/usr/bin/python3
"""modelando tabla"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """Definir la conexión con las tablas cities"""
    __tablename__ = "cities"
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
