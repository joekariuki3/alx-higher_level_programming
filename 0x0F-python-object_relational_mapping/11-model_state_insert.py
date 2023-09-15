#!/usr/bin/python3
'''
script that add a state
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
        newState = State('Louisiana')
        connectSession.add(newState)
        connectSession.commit()
        state = connectSession.query(State.id).filter(State.name ==
                                                      'Louisiana').first()

        if state:
            print(f"{state[0]}")
