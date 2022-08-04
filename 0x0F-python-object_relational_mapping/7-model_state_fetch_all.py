#!/usr/bin/python3
"""Listar todos los objetos State de 'hbtn_0e_6_usa' """

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
    for state in session.query(State).order_by(State.id).all():
        # HERE: no SQL query, only objects!
        print("{}: {}".format(state.id, state.name))
    session.close()
