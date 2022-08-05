#!/usr/bin/python3
"""crear State 'California:' 'San Francisco' hbtn_0e_100_usa"""
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

    new_obj = City(name="San Francisco", state=State(name="California"))

    session.add(new_obj)
    session.commit()
    session.close()
