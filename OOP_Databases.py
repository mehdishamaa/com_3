import pyodbc

class OOP_Database:

    def connection_parameters(self):                        # Pass in connection parameters
                                                        # Initialising connection using parameters
        server = 'databases2.spartaglobal.academy'
        database = 'Northwind'
        username = 'SA'
        password = 'Passw0rd2018'
        connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

    # Here we are creating a cursor for the connection

        cursor = connections.cursor()
        print("Connection Success!")
        return cursor # Takes the variable, running this method will be the output


object = OOP_Database()
object.connection_parameters()
