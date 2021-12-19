#!/usr/bin/python3
""" take in an arg and lists all values in the states table of
    hbtn_0e_0_usa where name matches the argument"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    con = MySQLdb.connect(
        host="localhost", user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3],
        charset="utf8")
    cur = con.cursor()
    cur.execute("SELECT * FROM states\
        WHERE name=%s ORDER BY id ASC", (sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    con.close()
