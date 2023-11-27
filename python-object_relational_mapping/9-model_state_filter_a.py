#!/usr/bin/python3
"""Lists all State objects containing the letter 'a' from the database"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # Creating a connection to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3],
                                  pool_pre_ping=True))

    # Creating a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Displaying the results
    for state in session.query(State).order_by(State.id):
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))

    # Closing the session
    session.close()
