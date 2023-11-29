#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)
    """Establishing a connection to the MySQL server"""

    Session = sessionmaker(bind=engine)
    session = Session()
    """Creating a session for database interaction"""

    query_result = session.query(City, State).filter(City.state_id == State.id).all()
    """Retrieving City-State pairs with matching state_id"""

    for city, state in query_result:
        """Displaying the results"""
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
    """Close the session"""
