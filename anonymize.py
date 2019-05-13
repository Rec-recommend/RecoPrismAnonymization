#!/usr/bin/python3

import pandas as pd

def anonymize( df , tableName ):
    tableHeader = tableName[0]
    df = renameColumnsHeader(df , tableHeader)
    return df

def renameColumnsHeader(df , tableHeader):
    char= 'a'
    for column in df.columns:
        df.rename(columns={column: char}, inplace=True)
        df = replaceColumnsData(df , char ,tableHeader)
        char = chr(ord(char) + 1)
    return df

def replaceColumnsData(df , column_name ,tableHeader):
    print(df[column_name])
    for index , value in enumerate(df[column_name]):
        df[column_name] = df[column_name].replace( value, tableHeader + column_name + str(index))
    return df

df = pd.read_csv("./titanic_train2.csv")
print(anonymize(df, "users").head())