#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Access to the database"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    """Create a cursor object to interact with the database"""
    cursor = db.cursor()

    """Execute the SQL query to retrieve all states"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """Fetch all the results of the query"""
    results = cursor.fetchall()

    """Display the results"""
    for row in results:
        print(row)

    """Close the cursor and the database connection"""
    cursor.close()
    db.close()