#!/usr/bin/python3
""" Select cities with names matching the specified state """

if __name__ == '__main__':
    """Check if the script is being run directly"""

    """Import necessary modules"""
    from sys import argv
    import MySQLdb

    """Extract MySQL username, password, database name, and user-specified state from command line arguments"""
    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    user_state = argv[4]

    """Connect to the MySQL server running on localhost at port 3306"""
    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=db_user,
                               passwd=db_passwd,
                               db=db_name)

    """Create a cursor object to interact with the database"""
    cursor = database.cursor()

    """Execute an SQL query to select cities.name from the 'cities' table
    joined with the 'states' table on cities.state_id = states.id
    where states.name matches the specified user_state, ordered by states.id in ascending order"""
    cursor.execute('SELECT cities.name FROM cities\
                   JOIN states\
                   ON cities.state_id = states.id\
                   WHERE states.name = %s\
                   ORDER BY states.id ASC', (user_state,))

    """Fetch all rows and store them in a list"""
    result = [value[0] for value in cursor.fetchall()]

    """Print the result as a comma-separated string"""
    print(', '.join(result))