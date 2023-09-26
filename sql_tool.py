# import sqlite3
# from sqlite3 import Error
import os

import mysql.connector as mysql
import yaml
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
    c.execute("SELECT  * FROM wechselabp")

    result = c.fetchall()
    return result


def get_parkplatzpublic(db):
    output = {}
    c = db.cursor(dictionary=True)
    c.execute("SELECT  * FROM parkplatz")

    result = c.fetchall()

    for row in result:
        if row["ParkplatzNr"] == 1:
            output["one"] = row

        elif row["ParkplatzNr"] == 2:
            output["two"] = row

        elif row["ParkplatzNr"] == 3:
            output["three"] = row

        elif row["ParkplatzNr"] == 4:
            output["four"] = row


        elif row["ParkplatzNr"] == 5:
         output["five"] = row
        elif row["ParkplatzNr"] == 6:
         output["six"] = row

    return result


home = os.environ['HOME']
try:
    with open(home + '/.config/dashboard/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

except:
    with open('./config.yaml', 'r') as file:
        config = yaml.safe_load(file)

# db = create_connection(user=config["user"], password=config["password"], database=config["database"], host=config["host"])


#print(get_user(db))
