#!/usr/bin/python3
"""Borrar un estado de la base de datos"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """no se ejecuta al importar"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)

    states_del = session.query(State).filter(State.name.contains("%a%")).all()

    for state in states_del:
        session.delete(state)

    session.commit()
    session.close()
