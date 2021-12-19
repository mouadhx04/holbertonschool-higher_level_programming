#!/usr/bin/python3
""" lists all states that's name starts with n from a database"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    con = MySQLdb.connect(
        host="localhost", user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3],
        charset="utf8")
    cur = con.cursor()
    cur.execute("SELECT * FROM states\
        WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(sys.argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    con.close()
