#!/usr/bin/python3
"""mostrar los valores donde la tabla coincidad con el argumnento"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    """No se ejecuta al ser importado"""
    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    conn = MySQLdb.connect(host='localhost', port=3306, user=user,
                           passwd=password, db=db_name,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
          ORDER BY id ASC".format(state_name))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
