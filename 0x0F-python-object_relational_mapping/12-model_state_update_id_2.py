#!/usr/bin/python3
"""Actualizar/cambiar el nombre de un estado"""

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

    parseData = session.query(State).filter(State.id == 2).all()

    if (len(parseData) == 0):
        print("Not found state to change")
    else:
        for state in parseData:
            state.name = "New Mexico"

    session.commit()
    session.close()
