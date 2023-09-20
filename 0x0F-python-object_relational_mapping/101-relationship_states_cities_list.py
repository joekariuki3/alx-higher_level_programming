#!/usr/bin/python3
"""
script that lists all states and its cities
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the states and its cities
    from the database.
    """
    db_uri = 'mysql://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    All = session.query(State, City).join(City).all()

    states = []

    # add state to a list
    for value in All:
        if value.State not in states:
            states.append(value.State)

    # print each state then look for its cities
    for state in states:
        print(f"{state.id}: {state.name}")
        for value in All:
            if state.id == value.City.state_id:
                print(f"    {value.City.id}: {value.City.name}")
    session.close()
