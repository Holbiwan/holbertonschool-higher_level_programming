#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
from sys import argv


if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=argv[1], passwd=argv[2], db=argv[3])
    """Connect to the MySQL server"""

    cursor = connection.cursor()
    """Creating a cursor object to execute queries"""

    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities "
                   "JOIN states "
                   "ON cities.state_id=states.id "
                   "ORDER BY cities.id ASC")
    """Executing the SELECT query to retrieve all cities"""

    lines = cursor.fetchall()
    """Fetch all the lines returned by the query"""

    for line in lines:
        """Print the results"""
        print(line)

    cursor.close()
    connection.close()
    """Close the cursor and the connection"""
