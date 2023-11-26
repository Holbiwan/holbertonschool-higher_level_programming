#!/usr/bin/python3
''' Script that lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa
'''

import MySQLdb
import sys

if __name__ == "__main__":

    ''' Connect to MySQL server running on localhosh at port 3306 '''
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    ''' Executing a SELECT query to retrieve all states with name
        starts with 'N' in case-sensitive manner
    '''

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                "ORDER BY states.id ASC")

    ''' Print results in the specified format '''
    for state in cur.fetchall():
        print(state)

    ''' Close the cursor and the database connection '''
    cur.close()
    db.close()