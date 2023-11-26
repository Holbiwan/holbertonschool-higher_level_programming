#!/usr/bin/python3
"""Script to list all states from the hbtn_0e_

"""Import necessary modules"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    """Check if the script is being run directly"""

    """Extract MySQL username, password, and database name from command line arguments"""
    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]

    """Connect to the MySQL server running on localhost at port 3306"""
    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=db_user,
                               passwd=db_passwd,
                               db=db_name)

    """Create a cursor object to interact with the database"""
    cursor = database.cursor()

    """Execute an SQL query to select id and name from the 'states' table, ordered by id in ascending order"""
    cursor.execute('SELECT id, name FROM states ORDER BY states.id ASC')

    """Iterate through the result set and print each row"""
    for row in cursor.fetchall():
        print(row)