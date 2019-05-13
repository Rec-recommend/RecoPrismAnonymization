import pandas as pd

def anonymize( data , tableName ):
    tableHeader = tableName[0]
    data = renameColumnsHeader(data , tableHeader)
    return data

def renameColumnsHeader(data , tableHeader):
    char= 'a'
    for column in data.columns:
        data.rename(columns={column: char}, inplace=True)
        data = replaceColumnsData(data , char ,tableHeader)
        char = chr(ord(char) + 1)
    return data

def replaceColumnsData(data , char ,tableHeader):
    for index , i in enumerate(data[char]):
        data[char] = data[char].replace( i, tableHeader + char + str(index))
    return data
