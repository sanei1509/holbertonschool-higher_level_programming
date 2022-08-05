#!/usr/bin/python3
"""imprimit todas las cities en City de  hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """no se ejecuta al importar"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)

    states_cities = session.query(State, City).join(City).order_by(City.id).all()

    for line in states_cities:
        print(f"{line[0].name}: ({line[1].id}) {line[1].name}")
    
    session.close()
