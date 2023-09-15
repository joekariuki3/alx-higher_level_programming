#!/usr/bin/python3
'''
script that lists all states using sqlalchemy
'''
from sqlalchemy import create_engine
from model_state import Base, State
import sys
if __name__ == '__main__':
    '''
    execute only when run as main
    '''
    userName = sys.argv[1]
    passWord = sys.argv[2]
    databaseName = sys.argv[3]

    engine = create_engine("mysql://{}:{}@localhost/{}".format(userName,
                           passWord, databaseName))
    results = engine.execute("SELECT * FROM states ORDER BY id")
    states = results.fetchall()

    for state in states:
        print(f"{state[0]}: {state[1]}")
