#!/usr/bin/python3
""" Modules used in this programm are sys and mysqldb"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    kd = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            password=argv[2], database=argv[3])
    cur = kd.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    db = cur.fetchall()
    for x in db:
        print(x)
