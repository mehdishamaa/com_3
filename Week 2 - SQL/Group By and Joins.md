**'`GROUP BY`' Pseudo Code:**

`SELECT` column_name(s) 
`FROM` table_name   
`WHERE` condition   
`GROUP` BY column_name(s)

**Example:**

`SELECT` `COUNT`(CustomerID), City  
`FROM` Customers    
`GROUP BY` City

The above code would result in us printing the number of customers per city.

**`HAVING` Pseudo Code:**

`SELECT` column_name(s)   
`FROM` table_name     
`WHERE` condition     
`GROUP` BY column_name(s)     
`HAVING` condition    
`ORDER BY` column_name(s) 






