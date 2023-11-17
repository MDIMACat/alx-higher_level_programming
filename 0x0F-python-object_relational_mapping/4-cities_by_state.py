#!/usr/bin/python3
""" script that lists all cities from the database
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
        port="3306",
        user=username,
        passwrd=password,
        db=db_name,
    )

    cursor = connection.cursor()
    query = "SELECT cities.id,\
                            cities.name,\
                            states.name\
                            FROM states INNER JOIN cities\
                            ON state_id = states.id\
                            ORDER BY cities.id;"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
