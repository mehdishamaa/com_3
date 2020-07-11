import pyodbc


# Database Connection Variables

server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Specifying the ODBC driver, server name, database, etc. directly

connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


print(type(rows))
print(rows[1])
print(rows.ProductName)

rows = query_result.fetchone()
print(type(rows))
print(rows[1])
print(rows.ProductName)