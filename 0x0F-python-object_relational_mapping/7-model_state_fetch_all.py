#!/usr/bin/python3
'''
script that lists all states using sqlalchemy
'''
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys
if __name__ == '__main__':
    '''
    execute only when run as main
    '''
    if (len(sys.argv) == 4):
        userName = sys.argv[1]
        passWord = sys.argv[2]
        databaseName = sys.argv[3]

        engine = create_engine("mysql://{}:{}@localhost/{}".format(userName,
                               passWord, databaseName))
        Session = sessionmaker(bind=engine)
        connectSession = Session()
        states = connectSession.query(State).all()

        for state in states:
            print(f"{state.id}: {state.name}")
