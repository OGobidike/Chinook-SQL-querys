# pylint: disable=invalid-name
'''Northwind queries'''

import sqlite3

# Connect to the northwind_small.sqlite3 database
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Queries
expensive_items = '''
SELECT * FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
'''

avg_hire_age = '''
SELECT AVG(HireDate - BirthDate) AS avg_hire_age
FROM Employee;
'''

ten_most_expensive = '''
SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product
JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY Product.UnitPrice DESC
LIMIT 10;
'''

largest_category = '''
SELECT Category.CategoryName, COUNT(DISTINCT Product.Id) AS product_count
FROM Product
JOIN Category ON Product.CategoryId = Category.Id
GROUP BY Category.CategoryName
ORDER BY product_count DESC
LIMIT 1;
'''

# Execute the queries and print results
if __name__ == "__main__":
    print("Ten most expensive items:")
    for row in curs.execute(expensive_items).fetchall():
        print(row)

    print("Average hire age:")
    print(curs.execute(avg_hire_age).fetchall())

    print("Ten most expensive items and their suppliers:")
    for row in curs.execute(ten_most_expensive).fetchall():
        print(row)

    print("Largest category by number of unique products:")
    print(curs.execute(largest_category).fetchall())
