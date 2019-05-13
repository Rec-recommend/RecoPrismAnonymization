def anonymize( data , tableName ):
    tableHeader = tableName[0]
    data = renameColumnsHeader(data , tableHeader)
    return data

def renameColumnsHeader(data , tableHeader):
    for column in data.columns:
            data.rename(columns={column: column[0]}, inplace=True)
            data = replaceColumnsData(data , column[0] ,tableHeader)
    return data
    
def replaceColumnsData(data , columnName ,tableHeader):
    for index , i in enumerate(data[columnName]):
        data[columnName] = data[columnName].replace( i, tableHeader + columnName + str(index))
    return data