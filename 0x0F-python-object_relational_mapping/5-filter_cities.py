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
    username, password, db_name, state_query = argv[1:5]

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
            SELECT cities.name
            FROM cities
            LEFT OUTER JOIN states
            ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """
    cursor.execute(query, (state_query,))

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Extract city names from the rows
    # cities = [row[0] for row in rows]

    # Print the results
    cities = []
    for row in rows:
        cities.append(row[0])

    # print the results as a comma-separated string
    print(", ".join(cities))

    # Close the cursor and database connection
    cursor.close()
    connection.close()
