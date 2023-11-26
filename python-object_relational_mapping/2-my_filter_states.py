#!/usr/bin/python3
''' Script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument
'''
import MySQLdb
import sys

if __name__ == "__main__":

    ''' Connect to the MySQL server running on localhost at port 3306 '''
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    ''' Construct the SQL query using format() and the state name argument '''
    state_name_searched = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}' "
                "ORDER BY states.id ASC".format(state_name_searched))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()