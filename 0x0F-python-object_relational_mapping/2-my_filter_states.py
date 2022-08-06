#!/usr/bin/python3
"""mostrar los valores donde la tabla coincidad con el argumnento"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    """No se ejecuta al ser importado"""
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=password, db=database,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM states WHERE name = '{state_name}'\
                ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
