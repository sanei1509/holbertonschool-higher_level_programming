#!/usr/bin/python3
"""
Listar todos los "states" de la database  "hbtn_0e_0usa"
"""
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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # HERE I have to know SQL to grab all states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
