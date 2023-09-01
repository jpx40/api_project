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
    with db.cursor(dictionary=True) as c:
        c.execute("SELECT  * FROM mitarbeiter")

        result = c.fetchall()

    return result


def get_game(db):
    with db.cursor(dictionary=True) as c:
        c.execute("SELECT  * FROM spiele")

        result = c.fetchall()

    return result




def get_arbeitzplatz(db):
    with db.cursor(dictionary=True) as c:
        c.execute("SELECT  * FROM wechselarbeitsplaetze")

        result = c.fetchall()
    return result


def get_parkplatz(db):
    output = {}
    with db.cursor(dictionary=True) as c:
        c.execute("SELECT  * FROM parkplatz")

        result = c.fetchall()




    for row in result:
        if row["parkplatz_id"] == 1:
            one = {"one": row}
            output["one"] = row

        elif row["parkplatz_id"] == 2:
            two = {"two": row}
            output["two"] = row

        elif row["parkplatz_id"] == 3:
            three = {"three": row}
            output["three"] = row

        elif row["parkplatz_id"] == 4:
            four = {"four": row}
            output["four"] = row


        elif row.parkplatz_id == 5:
            five = {"five": row}
            output["five"] = row

        elif row["parkplatz_id"] == 6:
            six = {"six": row}
            output["six"] = row

        elif row["parkplatz_id"] == 7:
            seven = {"eight": row}
            output["eight"] = row

        elif row["parkplatz_id"] == 8:
            eight = {"eight": row}
            output["eight"] = row

        elif row["parkplatz_id"] == 9:
            nine = {"nine": row}
            output["nine"] = row

    return output


