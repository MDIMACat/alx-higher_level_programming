#!/usr/bin/python3
"""
a script that lists all states from the database
ARGS: mysql username, mysql password and database name
"""


import MySQLdb
from sys import argv


if (__name__ == "__main__"):

    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM states")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
