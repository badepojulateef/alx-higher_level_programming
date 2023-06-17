#!/usr/bin/python3
"""
A script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    # Check that the script is being called correctly
    if (len(sys.argv) != 4):
        print("Usage: {} username password db_name".format(
            sys.argv[0])
        )
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

    try:
        # Query the database to find the states name containing a
        states_containing_a = session.query(State)\
                .filter(State.name.like("%a%")).all()
        # Update the state
        if states_containing_a is not None:
            for state in states_containing_a:
                # Delete the state object to be deleted
                session.delete(state)
        else:
            print("Not found")

        # Commit the session to the database
        session.commit()

    # Close the cursor abd database connection
    finally:
        session.close()
