#!/usr/bin/python3
"""a script that lists all states from the database
ARGS: mysql username, mysql password and database name"""


import MySQLdb
from sys import argv

#CHECK IF SCRIPT IS RUNNING DIRECTLY
if (__name__ == "__main__"):
    
    #ASSIGNING THE ARGUEMENTS PASSED
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    
    #ESTABLISH CONNECTION WITH DATABASE
    connection = MySQLdb.Connect(username, password, db_name)
    
    #CREATING THE CURSOR TO WRITE QUIERIES
    cursor = connection.cursor()
    
    #EXECUTING QUIERY
    cursor.execute("SELECT id, name FROM states")
    
    #FECTHES THE ROWS FROM DB
    rows = cursor.fetchall()
    
    #LOOP TO PRINT ROWS
    for row in rows:
        print(row)
    
    #CLOSE CURSOR
    cursor.close()
    
    #CLOSE CONNECTION
    connection.close()
    
