import pyodbc
import self as self

from OOP_Databases import OOP_Database


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
object.product_avg()
