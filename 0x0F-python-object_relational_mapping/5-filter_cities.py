#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    cities = ""

    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    with MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
    ) as connection:
        with connection.cursor() as cursor:
            query = "SELECT cities.name \
                     FROM states INNER JOIN cities \
                     ON states.id = state_id \
                     WHERE states.name = %s ORDER BY cities.id;"

            cursor.execute(query, (state_name,))

            for row in cursor.fetchall():
                cities += f"{row[0]}, "

    print(cities[0:-2])
