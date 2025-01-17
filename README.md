# 🖈️ Chinook Querys: A Data Explorer's Dream!

Welcome to **Northwind Queries**, a project dedicated to unearthing insights from the iconic Northwind database. Through a series of carefully crafted SQL queries, this project reveals fascinating details about products, suppliers, employees, and categories—all wrapped in a fun, data-driven package! 🎮

---

## 🔧 Tech Stack

- **SQLite3**: A lightweight and powerful database solution.  
- **Python**: For scripting, query execution, and reporting.  
- **SQL**: The backbone of data exploration and analysis.  

---

## 🔍 Query Highlights & Insights

### 🎁 Top 10 Most Expensive Items

**Objective**: Discover the priciest products in the inventory.  

```sql
SELECT * FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
```

### 🎉 Average Hire Age of Employees

**Objective**: Calculate the average age of employees at the time of hiring.  

```sql
SELECT AVG(HireDate - BirthDate) AS avg_hire_age
FROM Employee;
```
### 🛒 Top 10 Most Expensive Products & Their Suppliers

**Objective**: Match the 10 most expensive products with their respective suppliers.  

```sql
SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product
JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY Product.UnitPrice DESC
LIMIT 10;
```
### 🏋️‍♂️ Largest Product Category

**Objective**: Identify the category with the highest number of unique products.  

```sql
SELECT Category.CategoryName, COUNT(DISTINCT Product.Id) AS product_count
FROM Product
JOIN Category ON Product.CategoryId = Category.Id
GROUP BY Category.CategoryName
ORDER BY product_count DESC
LIMIT 1;
```

---

## 🔧 Setup & Execution

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/Northwind-Queries
   cd Northwind-Queries
   ```

2. **Ensure Dependencies**:
   - Install Python if not already available.
   - Verify SQLite3 is installed.

3. **Run the Script**:
   ```bash
   python northwind.py
   ```

4. **Explore the Results**: Watch the magic unfold in your terminal as insights come to life! 🌟

---

## 🎮 Why This Project?

- **Real-World Application**: Gain practical insights into a dataset modeled after real-world business scenarios.  
- **SQL Practice**: Hone your SQL skills by exploring queries that address business-critical questions.  
- **Storytelling with Data**: Translate numbers into narratives that inform decision-making.  

---

## 🚀 To Explore the Data? Or not to explore, that is the question...

Uncover the hidden stories in Northwind! Clone the repo, run the queries, and become a data detective! 🕵️‍♂️

Feel free to contribute, fork, or suggest improvements. I'm a little new at this so if u encounter any debuggery pls be gentle! 🌈

