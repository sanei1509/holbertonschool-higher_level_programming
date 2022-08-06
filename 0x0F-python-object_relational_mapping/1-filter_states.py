#!/usr/bin/python3
"Listar todos los estados con nombres que empiecen con N de hbtn_0e_0_usa"
import MySQLdb
import sys

if __name__ == "__main__":
    """No se ejecuta cuando es importado"""

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                       passwd=mysql_password, db=database_name, charset="utf8")

cur = conn.cursor()
cur.execute("SELECT *FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
