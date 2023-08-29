import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None

    try:

        connection = sqlite3.connect(path)

        print("Connection to SQLite DB successful")

    except  Error as e:

        print(f"The error '{e}' occurred")

    return connection


connection = create_connection("./test.db")
connection.row_factory = sqlite3.Row


def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


def get_user(conn):
    result = []
    conn.row_factory = dict_factory
    for row in conn.execute("SELECT  * from 'user'"):
        result.append(row)

    return result


def get_game(conn):
    result = []
    conn.row_factory = dict_factory
    for row in conn.execute("SELECT  * from 'game'"):
        result.append(row)

    return result


def db_close(conn):
    result = []
    conn.row_factory = dict_factory
    for row in conn.execute("SELECT  * from 'user'"):
        result.append(row)


def get_arbeitzplatz(conn):
    result = []
    conn.row_factory = dict_factory
    for row in conn.execute("SELECT  * from 'arbeitzplatz'"):
        result.append(row)
    return result


def get_parkplatz(conn):
    result = []
    conn.row_factory = dict_factory
    for row in conn.execute("SELECT  * from 'parkplatz'"):
        result.append(row)
    return result
