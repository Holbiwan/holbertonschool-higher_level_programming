#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state name>"
              .format(argv[0]))
    else:
        username = argv[1]
        password = argv[2]
        database = argv[3]
        state_name = argv[4]

        """Connect to the MySQL server"""
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, database),
                               pool_pre_ping=True)

        """Create a session to interact with the database"""
        Session = sessionmaker(bind=engine)
        session = Session()

        """Query the State table for the given state_name"""
        state = (session.query(State)
                 .filter(State.name == state_name)
                 .first())

        if state:
            """Print the state's id if found"""
            print("{}".format(state.id))
        else:
            """Print "Not found" if no state with the given name is found"""
            print("Not found")

        """Close the session"""
        session.close()
