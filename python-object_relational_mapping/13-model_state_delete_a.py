#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
with a from the db hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker, Session
from model_state import Base, State

if __name__ == "__main__":
    """Get the command line arguments"""
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    """Create the connection string to the MySQL server"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(mysql_username, mysql_password, database_name),
                           pool_pre_ping=True)

    """Create a session"""
    session = Session(engine)

    """Delete all State objects with a name containing the letter 'a'"""
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    """Close the session"""
    session.close()
