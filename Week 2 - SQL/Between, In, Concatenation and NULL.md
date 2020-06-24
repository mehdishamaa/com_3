`SELECT` c.CompanyName, c.City, c.Country, c.Region

`FROM` Customers c

`WHERE` c.Region='BC'

- The above shows us the company name and city from the customers table in the BC region.
- Using 'c.' is known as 'Table Aliasing'

--------
`SELECT TOP` 100 

- This allows us to query very large databases without performance issues

-----
`SELECT` p.ProductName, p.UnitPrice

`FROM` Products p

`WHERE`p.CategoryID = 1 `AND` p.Discontinued = 0

- This code shows us product names and prices of products in a certain category which are discontinued

