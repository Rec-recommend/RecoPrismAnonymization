#!/usr/bin/python3

import pandas as pd
import mysql.connector

def prepare_data(_host, _user, _password, _database , table_name):

    db = mysql.connector.connect(
        host = _host,
        user = _user,
        password = _password,
        database = _database
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM " + table_name)

    df = pd.DataFrame(cursor.fetchall())

    df.columns = cursor.column_names

    db.close()

    return df