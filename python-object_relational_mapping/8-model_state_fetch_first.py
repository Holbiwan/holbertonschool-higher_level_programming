#!/usr/bin/python3
"""Prints the first State objects from the database hbtn_0e_6_usa"""

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm.session import sessionmaker, Session
    from model_state import Base, State

    username = '{}'.format(argv[1])
    password = '{}'.format(argv[2])
    db_name = '{}'.format(argv[3])

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))
    """Connect to mySQL server"""

    Session = sessionmaker(bind=engine)
    """Setting up a session to interact with the database"""
    session = Session()

    result = session.query(State).order_by(State.id).first()
    if result:
        """Show the results"""
        print('{}: {}'.format(result.id, result.name))
    else:
        print('Nothing')
