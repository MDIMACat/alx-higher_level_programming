#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database
"""


import MySQLdb
from sys import argv

if (__name__ == "__main__"):

    cities = ""

    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwrd=password,
        db=db_name,
    )

    cursor = connection.cursor()
    query = "SELECT cities.name\
                            FROM states INNER JOIN cities\
                            ON states.id = state_id\
                            WHERE states.name = %s;"
    cursor(query, state_name)
    rows = cursor.fetchall()

    for row in rows:
        cities += f"{row[0]}, "

    print(cities[0:-2])

    cursor.close()
    connection.close()
