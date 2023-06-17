#!/usr/bin/python3
"""
A script that lists all states from the
database hbtn_0e_0_usa using sqlalchemy
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    # Check that the script is being called correctly
    if (len(sys.argv) != 5):
        print("Usage: {} username password db_name state_query".format(
            sys.argv[0])
        )
        sys.exit(1)

    # Parse the command line arguments and
    # Get MySQL credentials from command line
    # arguments
    username, password, db_name, state_query = sys.argv[1:5]
    host = "localhost"
    driver_name = "mysql+mysqldb"

    # Connect to MySQL server
    engine = create_engine(
                "{}://{}:{}@{}/{}"
                .format(
                    driver_name,
                    username,
                    password,
                    host,
                    db_name
                ),
                pool_pre_ping=True
            )

    # Create the table(s) associated with the defined classes
    Base.metadata.create_all(engine)

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query a session factory bound to the engine
    try:
        state = session.query(State).filter(State.name == state_query).first()
        if state is not None:
            print(state.id)
        else:
            print("Not found")

    # Close the cursor abd database connection
    finally:
        session.close()
