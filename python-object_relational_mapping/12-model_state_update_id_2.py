#!/usr/bin/python3
"""Changes name of a State object from the database hbtn_0e_6_usa"""

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    username = '{}'.format(argv[1])
    password = '{}'.format(argv[2])
    db_name = '{}'.format(argv[3])

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))
    """Create a connection to the MySQL server"""

    Session = sessionmaker(bind=engine)
    session = Session()
    """Create a session to interact with the database"""

    session.query(State).filter(State.id == 2).update({'name': 'New Mexico'})

    session.commit()

    session.close()
    """Close the session"""
