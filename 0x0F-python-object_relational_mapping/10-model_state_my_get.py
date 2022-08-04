#!/usr/bin/python3
"""Mostrar el 'state' con el nombre pasado por argumento"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """no se ejecuta al importar"""
    state_name = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()

    session = Session(bind=engine)
    cont = 0
    parseData = session.query(State).filter(State.name == state_name).all()
    # HERE: no SQL query, only objects!
    if len(parseData) == 0:
        print("Not found")
    else:
        for state in parseData:
            print(state.id)

    session.close()
