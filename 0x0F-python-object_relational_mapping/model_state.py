#!/usr/bin/python3
'''
get sqlalchemy and also the base class
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

'''
declare the base class
'''
Base = declarative_base()


class State(Base):
    '''
    State class inherits from the base
    '''
    __tablename__ = 'states'
    id = Column("id", Integer, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)

    def __init__(self, name):
        '''
        initialize the state class
        '''
        self.name = name
