- **'`GROUP BY`' Pseudo Code:**


`SELECT` column_name(s) 
`FROM` table_name   
`WHERE` condition   
`GROUP` BY column_name(s)

- **Example:**


`SELECT` `COUNT`(CustomerID), City  
`FROM` Customers    
`GROUP BY` City

The above code would result in us printing the number of customers per city.


- **`HAVING` Pseudo Code:**


`SELECT` column_name(s)   
`FROM` table_name     
`WHERE` condition     
`GROUP` BY column_name(s)     
`HAVING` condition    
`ORDER BY` column_name(s) 

**Example:**

`SELECT` `COUNT`(CustomerID), City  
`FROM` Customers  
`GROUP BY` City   
`HAVING COUNT`(CustomerID) > 2  

the above example would list all cities with more than two customers.


**`SELECT` Statement Processing Sequence:**  

1) `SELECT`
2) `DISTINCT`
3) `FROM`
4) `WHERE`
5) `GROUP BY`
6) `HAVING`
7) `ORDER BY`

-----

###### **Joins - When to use which type?:**


[Joins](https://www.dofactory.com/Images/sql/sql-joins.png)

**Inner Joins:**

`SELECT` column-names 
`FROM` table-name1    
`INNER JOIN` table-name2 ON column-name1 = column-name2   
`WHERE` condition 




