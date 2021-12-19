#!/usr/bin/python3

"""
Select all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

def print_states():

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
