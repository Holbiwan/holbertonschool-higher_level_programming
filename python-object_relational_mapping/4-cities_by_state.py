#!/usr/bin/python3
""" Select states with names matching arguments """

if __name__ == '__main__':
    """Check if the script is being run directly"""

    """Import necessary modules"""
    from sys import argv
    import MySQLdb

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

    """Execute an SQL query to select cities.id, cities.name, and states.name from the 'cities' table
    joined with the 'states' table on cities.state_id = states.id, ordered by cities.id in ascending order"""
    cursor.execute('SELECT cities.id, cities.name, states.name FROM cities\
                   JOIN states\
                   ON cities.state_id = states.id\
                   ORDER BY cities.id ASC')

    """Iterate through the result set"""
    for row in cursor.fetchall():
        """Print each row"""
        print(row)