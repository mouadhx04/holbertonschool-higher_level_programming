#!/usr/bin/python3
""" list all cities from the database hbtn_0e_4_usa """


if __name__ == "__main__":
    import MySQLdb
    import sys
    con = MySQLdb.connect(
        host="localhost", user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3],
        charset="utf8")
    cur = con.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
        FROM states\
        INNER JOIN cities ON states.id = cities.state_id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    con.close()
