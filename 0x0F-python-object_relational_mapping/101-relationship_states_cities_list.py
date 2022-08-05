#!/usr/bin/python3
"""Listar los estados y sus respectivas ciudades"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    """No se va a ejecutar al importar"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)

    obj_data = session.query(State).order_by(State.id).all()

    for states in obj_data:
        print(f"{states.id}: {states.name}")
        for city in states.cities:
            print(f"    {city.id}: {city.name}")

    session.close()
