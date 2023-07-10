#!/usr/bin/python3
"""
simple MyInt class 
inherits from int
"""
class MyInt(int):
    def __eq__(self, num):
        return super().__eq__(num)

    def __ne__(self, num):
        return super().__ne__(num)
