#!/usr/bin/python3
"""Deletes all State objects with a name
   containing the letter 'a' from the database."""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Get the command line arguments"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]
        ),
        pool_pre_ping=True
    )
    """Creating the connection string to the MySQL server"""

    Session = sessionmaker(bind=engine)
    session = Session()
    """Creating a session to interact with the database"""

    state_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in state_delete:
        session.delete(state)

    """Delete State objects with a name containing 'a'"""

    session.commit()

    session.close()
    """Close the session"""
