#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Get data from command line
    """
    username, password, db_name = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
           sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
       )

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))

    Base.metadata.create_all(engine)
