#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)
    """Establishing a connection to the MySQL server"""

    Session = sessionmaker(bind=engine)
    session = Session()
    """Creating a session for database interaction"""

    query_lines = session.query(City, State).\
        filter(City.state_id == State.id).all()
    """Retrieving City-State pairs objects with matching stade_id"""

    for city, state in query_lines:
        """Show the results"""
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
    """Close the session"""
