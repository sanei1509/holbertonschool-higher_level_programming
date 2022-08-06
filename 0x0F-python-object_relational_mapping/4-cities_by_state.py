#!/usr/bin/python3
"""Listar 'cities' de la database 'hbtn_0e_4_usa' """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    """No se ejecuta al ser importado"""
    user = argv[1]
    password = argv[2]
    db_name = argv[3]

    conn = MySQLdb.connect(host='localhost', port=3306, user=user,
                           passwd=password, db=db_name,
                           charset="utf8")
    cur = conn.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities JOIN states ON cities.state_id = states.id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
