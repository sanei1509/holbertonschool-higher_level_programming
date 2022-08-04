#!/usr/bin/python3
"""script que imprima el 1er State de 'hbtn_0e_6_usa' """

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
    cont = 0
    for state in session.query(State).order_by(State.id).all():
        # HERE: no SQL query, only objects!
        cont += 1
        if cont == 1:
            print("{}: {}".format(state.id, state.name))
        if cont == 0:
            print()
            break

    session.close()
