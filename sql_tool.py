# import sqlite3
# from sqlite3 import Error
import mysql.connector as mysql
from mysql.connector import Error


def create_connection(password: str, user: str, database: str, host: str):
    connection = None

    try:

        connection = mysql.connect(user=user, password=password,
                                   host=host,
                                   database=database)

        print("Connection to mysql DB successful")

    except  Error as e:

        print(f"The error '{e}' occurred")

    return connection


def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


def get_user(db):
    c = db.cursor(dictionary=True)
    c.execute("SELECT  * FROM mitarbeiter")

    result = c.fetchall()
    return result


def get_game(db):
    c = db.cursor(dictionary=True)
    c.execute("SELECT  * FROM spiele")

    result = c.fetchall()

    return result


def get_arbeitzplatz(db):
    c = db.cursor(dictionary=True)
    c.execute("SELECT  * FROM wechselarbeitzplatz")

    result = c.fetchall()
    return result



def get_parkplatzpublic(db):
    output = {}
    c = db.cursor(dictionary=True)
    c.execute("SELECT  * FROM parkplatzpublic")

    result = c.fetchall()

    for row in result:
        if row["parkplatz_id"] == 1:
            output["one"] = row

        elif row["parkplatz_id"] == 2:
            output["two"] = row

        elif row["parkplatz_id"] == 3:
            output["three"] = row

        elif row["parkplatz_id"] == 4:
            output["four"] = row


        elif row["parkplatz_id"] == 5:
         output["five"] = row
        elif row["parkplatz_id"] == 6:
         output["six"] = row

    return output

db = create_connection(user="Jonas_P", password="Password", database="sys", host="10.0.0.200")

print(get_parkplatzpublic(db))
