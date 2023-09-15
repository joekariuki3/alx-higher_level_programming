#!/usr/bin/python3
'''
script that lists  states using sqlalchemy
'''
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys
if __name__ == '__main__':
    '''
    execute only when run as main
    '''
    if (len(sys.argv) == 5):
        userName = sys.argv[1]
        passWord = sys.argv[2]
        databaseName = sys.argv[3]
        stateName = sys.argv[4]

        engine = create_engine("mysql://{}:{}@localhost/{}".format(userName,
                               passWord, databaseName))
        Session = sessionmaker(bind=engine)
        connectSession = Session()
        state = connectSession.query(State.id).filter(State.name ==
                                                      stateName).first()

        if state:
            print(f"{state[0]}")
        elif not state:
            print("Not found")
