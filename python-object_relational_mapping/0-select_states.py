#!/usr/bin/python3
''' Script that lists all states from the database hbtn_0e_0_usa '''
import MySQLdb
import sys

if __name__ == "__main__":

    ''' Connect to MySQL server running locally on port 3306 '''
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    ''' Execute an SQL query to fetch all states '''
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    ''' Print the results in the desired format '''
    for state in cur.fetchall():
        print(state)

    ''' Close the cursor and the connection to the database '''
    cursor.close()
    db.close()
