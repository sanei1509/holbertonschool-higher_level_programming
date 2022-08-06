#!/usr/bin/python3
"Listar todos los estados con nombres que empiecen con N de hbtn_0e_0_usa"
from sys import argv
import MySQLdb

if __name__ == "__main__":
    """No se ejecuta cuando es importado"""
    user = argv[1]
    password = argv[2]
    name = argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=password, db=name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT *FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
