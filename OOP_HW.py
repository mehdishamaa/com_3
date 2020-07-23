import pyodbc
import self as self

# Here we are importing our OOP_Database class from OOP_Databases file
from OOP_Databases import OOP_Database

# Next we create a Queries class

class Queries:

    def product_query(self):
        object = OOP_Database()
        cursor = object.connection_parameters()
        cursor.execute("SELECT ProductID, ProductName FROM Products")
        products = cursor.fetchall()
        for product in products:
            print(product)

    def product_avg(self):
        object = OOP_Database()
        cursor = object.connection_parameters()
        cursor.execute("SELECT AVG(UnitPrice) FROM Products")
        product_avg = cursor.fetchall()
        for avg in product_avg:
            print(avg)

       
object = Queries()
object.product_query()
