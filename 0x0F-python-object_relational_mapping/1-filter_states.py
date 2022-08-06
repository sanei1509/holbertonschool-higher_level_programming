#!/usr/bin/python3
"Listar todos los estados con nombres que empiecen con N de hbtn_0e_0_usa"

if __name__ == "__main__":
    """ No se ejecuta al ser importado """
    import MySQLdb
    from sys import argv
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'
                ORDER BY states.id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
