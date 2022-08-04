#!/usr/bin/python3
"""Listar 'cities' de la database 'hbtn_0e_4_usa' """

import MySQLdb
import sys
if __name__ == "__main__":
    """No se ejecuta cuando es importado"""
    user = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]

conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                       passwd=passw, db=db, charset="utf8")

cur = conn.cursor()
cur.execute("SELECT cities.id, cities.name, states.name\
            FROM cities JOIN states ON cities.state_id = states.id")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
