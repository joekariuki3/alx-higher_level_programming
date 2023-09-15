#!/usr/bin/python3
'''
script to list all states from the database
'''
if __name__ == '__main__':
    '''
    if run as main then execute
    '''
    import MySQLdb
    import sys

    if (len(sys.argv) == 4):
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # connect to the database
        db = MySQLdb.connect(host='localhost', port=3306, user=username,
                             passwd=password, db=database)

        # create a cursor to use to read info in the database
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id")

        # select all info from the table state
        statesList = cur.fetchall()

        # print states
        for state in statesList:
            print(state)
