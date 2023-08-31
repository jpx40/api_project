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
    output = {}
    conn.row_factory = dict_factory
    for row in conn.execute("SELECT  * from 'parkplatz'"):
        result.append(row)
    for row in result:
        if row["parkplatz_id"] == 1:
            one = {"one": row}
            output["one"] = row

        elif row["parkplatz_id"] == 2:
            two ={"two": row}
            output["two"] = row

        elif row["parkplatz_id"] == 3:
            three ={"three": row}
            output["three"] = row

        elif row["parkplatz_id"] == 4:
            four ={"four": row}
            output["four"] = row


        elif row.parkplatz_id == 5:
            five ={"five": row}
            output["five"] = row

        elif row["parkplatz_id"] == 6:
            six ={"six": row}
            output["six"] = row

        elif row["parkplatz_id"] == 7:
            seven ={"eight": row}
            output["eight"] = row

        elif row["parkplatz_id"] == 8:
            eight ={"eight": row}
            output["eight"] = row

        elif row["parkplatz_id"] == 9:
            nine ={"nine": row}
            output["nine"] = row





    return output
