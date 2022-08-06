#!/usr/bin/python3
"""Listar todas las ciudades tomadas como argumnento"""
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
    cur.execute("SELECT cities.name\
                FROM cities JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id ASC", (state_name,))
    query_rows = cur.fetchall()
    text = ""
    cont = 0
    for row in query_rows:
        cont += 1
        if cont < len(query_rows):
            text += row[0]+', '
        else:
            text += row[0]
    print(text)
    cur.close()
    conn.close()
