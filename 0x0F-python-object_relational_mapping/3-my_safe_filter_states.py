#!/usr/bin/python3
"""Prevenir la inyection of code in the task 3"""

import MySQLdb
import sys
if __name__ == "__main__":
    """No se ejecuta cuando es importado"""
    _user = argv[1]
    _password = argv[2]
    db_name = argv[3]
    state = argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=_user,
                           passwd=_password, db=db_name, charset="utf8")

    cur = conn.cursor()
    cur.execute(f"SELECT *FROM states WHERE name = %s\
                ORDER BY id ASC;", (stateName_search,))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
