#!/usr/bin/python3
"""Listar todas las ciudades tomadas como argumnento"""

import MySQLdb
import sys
if __name__ == "__main__":
    """No se ejecuta cuando es importado"""
    user = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]
state_name = sys.argv[4]

conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                       passwd=passw, db=db, charset="utf8")

cur = conn.cursor()
cur.execute("SELECT cities.name\
            FROM cities JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s ORDER BY cities.id ASC", (state_name,))
query_rows = cur.fetchall()
text = ""
cont = 0
for row in query_rows:
    cont += 1
    if cont < 3:
        text += row[0]+', '
    else:
        text += row[0]
print(text)
cur.close()
conn.close()
