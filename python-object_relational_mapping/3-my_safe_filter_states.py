#!/usr/bin/python3
""" Select states with names matching arguments """

if __name__ == '__main__':
    """Check if the script is being run directly"""

    """Import necessary modules"""
    from sys import argv
    import MySQLdb

    """Extract MySQL username, password, database name, and search term from command line arguments"""
    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    
    # Format the search term from command line argument
    search = '{}'.format(argv[4])

    """Connect to the MySQL server running on localhost at port 3306"""
    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=db_user,
                               passwd=db_passwd,
                               db=db_name)

    """Create a cursor object to interact with the database"""
    cursor = database.cursor()

    """Execute an SQL query to select id and name from the 'states' table
    where the name matches the specified search term, ordered by id in ascending order"""
    cursor.execute('SELECT id, name FROM states\
                   WHERE name = %s\
                   ORDER BY states.id ASC;', (search,))

    """Iterate through the result set"""
    for row in cursor.fetchall():
        """Print each row"""
        print(row)