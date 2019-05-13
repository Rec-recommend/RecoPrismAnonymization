import pandas as pd
import mysql.connector

from anonymize import anonymize
from saveToCSV import saveDataToCSV

def read_from_db(_host, _user, _password, _database , table_name):

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

def read_from_csv(csv_path):
    return pd.read_csv(csv_path)

def startAnonymize(df, table_name):
    data = anonymize( df , table_name )
    saveDataToCSV( data , table_name )