#!/usr/bin/python3
"""
lists all cities
"""
if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute(""" SELECT cities.id, cities.name, states.name
                FROM cities INNER JOIN states ON
                cities.state_id = states.id
                WHERE states.name LIKE %s
                ORDER BY cities.id ASC
    """, (argv[4], ))
    query_rows = cur.fetchall()
    print(', '.join(row[1] for row in query_rows))
    cur.close()
    db.close()
