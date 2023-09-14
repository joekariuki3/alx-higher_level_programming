#!/usr/bin/python3
# script to list all cities from the database
if __name__ == '__main__':
    import MySQLdb
    import sys

    if (len(sys.argv) == 4):
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # connect to the database
        db = MySQLdb.connect(host='localhost', user=username,
                             passwd=password, db=database)

        # create a cursor to use to read info in the database
        cur = db.cursor()
        cur.execute('''SELECT cities.id, cities.name,
                    states.name FROM cities INNER JOIN states
                    ON cities.state_id=states.id ORDER BY id''')

        # select all info from the table state
        statesList = cur.fetchall()

        # print states
        for state in statesList:
            print(state)
