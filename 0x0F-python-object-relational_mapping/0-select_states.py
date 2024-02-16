#!/usr/bin/python3
"""
    script to get all states
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
            user = username, passwd=password, db=db_name)
    cur = db.cursor()
    r = cur.execute("SELECT * FROM states ORDER BY id ASC")
    for state in r:
        print(state)
