#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
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
    query = "SELECT * FROM {}.states ORDER BY id ASC".format(db_name)
    cursor.execute(query)

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    connection.close()
