#!/usr/bin/python3
""" take in the name of a state as an argument and lists all cities"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    con = MySQLdb.connect(
        host="localhost", user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3],
        charset="utf8")
    cur = con.cursor()
    cur.execute("SELECT cities.name FROM cities\
        INNER JOIN states ON states.id = cities.state_id\
        WHERE states.name=%s", (sys.argv[4],))
    query_rows = cur.fetchall()
    if len(query_rows) == 0:
        print()
    else:
        for i in range(len(query_rows)):
            if i == len(query_rows) - 1:
                print(query_rows[i][0])
            else:
                print(query_rows[i][0], end=", ")
    cur.close()
    con.close()
