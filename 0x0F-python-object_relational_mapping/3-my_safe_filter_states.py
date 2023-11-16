#!/usr/bin/python3
"""
A script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name_searched = argv[4]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
    )

    cursor = connection.cursor()

    query = "SELECT id, name FROM states WHERE BINARY name = %s;"
    cursor.execute(query, (state_name_searched,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
