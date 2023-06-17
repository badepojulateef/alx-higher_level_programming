#!/usr/bin/python3
"""
A script that lists all State objects, and
corresponding City objects, contained in
the database hbtn_0e_101_usa using sqlalchemy
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Check that the script is being called correctly
    if (len(sys.argv) != 4):
        print("Usage: {} username password db_name".format(sys.argv[0]))
        sys.exit(1)

    # Parse the command line arguments and
    # Get MySQL credentials from command line
    # arguments
    username, password, db_name = sys.argv[1:4]
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
        states = session.query(State).order_by(State.id).all()

        # Display the results
        if states is not None:
            for state in states:
                print("{}: {}".format(state.id, state.name))
                for city in state.cities:
                    print("\t{}: {}".format(city.id, city.name))
        else:
            print("Not found")

    # Close the cursor abd database connection
    finally:
        session.close()
