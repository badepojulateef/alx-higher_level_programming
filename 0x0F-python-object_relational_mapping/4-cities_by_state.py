#!/usr/bin/python3
"""
A script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the
argument
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials from command line
    username, password, db_name = argv[1:4]

    # Connect to MySQL server
    connection = MySQLdb.connect(
                user=username,
                passwd=password,
                db=db_name,
                host="localhost",
                port=3306
            )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute the SQL query
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            LEFT OUTER JOIN states
            ON cities.state_id = states.id
            ORDER BY id ASC
            """
    cursor.execute(query)

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    connection.close()
