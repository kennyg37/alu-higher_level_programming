#!/usr/bin/python3
""" fetches all the names starting by m in the database"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            password=argv[2], database=argv[3])
    cu = conn.cursor()
    cu.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    kd = cursor.fetchall()
    for x in kd:
        print(x)
