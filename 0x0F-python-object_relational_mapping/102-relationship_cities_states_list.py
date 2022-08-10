#!/usr/bin/python3
"""
Listar toda la lista de ciudades de la db hbtn_0e_101_usa:
"""
import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    all_data = session.query(State.name, City.id, City.name).join(City).all()

    for state_city in all_data:
        print(f"{state_city[1]}: {state_city[2]} -> {state_city[0]}")

    session.close()
