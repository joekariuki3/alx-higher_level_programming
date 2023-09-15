#!/usr/bin/python3
'''
get sqlalchemy, base and also the state class
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    '''
    City class inherits from the base
    '''
    __tablename__ = 'cities'
    id = Column("id", Integer, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, ForeignKey(State.id),
                      nullable=False)

    def __init__(self, name):
        '''
        initialize the City class
        '''
        self.name = name
        self.state = State.id
