#!/usr/bin/python3
"""mostrar los valores donde la tabla coincidad con el argumnento"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    """No se ejecuta cuando es importado"""
    state_name = str(argv[4])

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3],
                           charset="utf8")

    cur = conn.cursor()
    cur.execute(f"SELECT * FROM states WHERE name LIKE '{state_name}'\
                ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
