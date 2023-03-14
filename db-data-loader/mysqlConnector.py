import mysql.connector
from mysql.connector import Error

# class Database:
def dbConnect():
    try:
        dbcon = mysql.connector.connect(
            host='localhost',
            database='test_db',
            user='root',
            password=''
        )
        c = dbcon.cursor(dictionary=True)
        return dbcon, c
    except Error as e:
            print("Error while connecting to MySQL", e)