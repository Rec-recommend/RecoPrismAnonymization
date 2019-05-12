def anonymize( data , tableName ):
    tableHeader = tableName[0]
    # print(tableHeader)
    # print(data.columns[0])
    data = renameColumnsHeader(data)
        # print(column)
    # print(data.columns)
    return data

def renameColumnsHeader(data):
    for column in data.columns:
            data.rename(columns={column: column[0]}, inplace=True)
    return data
    
def replaceColumnsData(data):
