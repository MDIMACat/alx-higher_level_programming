#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    with MySQLdb.connect(
        user=username,
        passwd=password,
        db=db_name
    ) as connection:
        cursor = connection.cursor()

        query = """
                SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id;
                """

        cursor.execute(query, (state_name,))

        cities = cursor.fetchall()

        cursor.close()

    if cities:
        print(", ".join(city[0] for city in cities))
