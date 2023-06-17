#!/usr/bin/python3
"""
A script that prints all City objects from
the database hbtn_0e_14_usa using sqlalchemy
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State
from model_city import City

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
        res = session.query(State, City).join(City).order_by(City.id)
        if res is not None:
            for state, city in res:
                print("{}: ({}) {}".format(state.name, city.id, city.name))
        else:
            print("Not found")

    # Close the cursor abd database connection
    finally:
        session.close()
