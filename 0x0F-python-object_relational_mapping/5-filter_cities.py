#!/usr/bin/python3
'''
script that takes in arguments of a state name
and lists all cities in that state
'''
import MySQLdb
import sys

if __name__ == '__main__':
    '''
    if it is run as main then it will run the following
    '''
    if (len(sys.argv) == 5):
        userName = sys.argv[1]
        passWord = sys.argv[2]
        databaseName = sys.argv[3]
        stateName = sys.argv[4]

        db = MySQLdb.connect(host='localhost', port=3306, user=userName,
                             passwd=passWord, database=databaseName)

        cur = db.cursor()
        query = ('''SELECT cities.name FROM cities
                 WHERE state_id = (SELECT id FROM states WHERE name=%s)''')
        cur.execute(query, (stateName, ))
        cities = cur.fetchall()
        i = 0
        for city in cities:
            print(f"{city[0]}", end='')
            if i < len(cities) - 1:
                print(", ", end='')
            i = i + 1
        print()
        cur.close()
        db.close()
