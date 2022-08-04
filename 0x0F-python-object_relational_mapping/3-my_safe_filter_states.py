#!/usr/bin/python3
"""Prevenir la inyection of code in the task 3"""

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
cur.execute(f"SELECT * FROM states WHERE name = %s\
ORDER BY id ASC", (state_name,))
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
