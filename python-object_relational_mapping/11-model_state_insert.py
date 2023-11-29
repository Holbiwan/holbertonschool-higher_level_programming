#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """Get the command line arguments"""
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    """Create the connection string to the MySQL server"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            mysql_username, mysql_password, database_name),
        pool_pre_ping=True
    )

    """Create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Add a new State to the database"""
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    """Print the new state's ID after creation"""
    print(new_state.id)

    """Close the session"""
    session.close()
