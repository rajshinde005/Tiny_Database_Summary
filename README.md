# 🧾 Task 7: Basic Sales Summary using SQLite and Python

## 🎯 Objective
Use **SQL inside Python** to extract simple sales insights (like total quantity and total revenue)
and visualize them using a bar chart.

---

## 🛠️ Tools Used
- Python (with `sqlite3`, `pandas`, `matplotlib`)
- SQLite (built-in with Python, no installation needed)
- VS Code or Jupyter Notebook

---

## 📂 Dataset
A small SQLite database (`sales_data.db`) with a single table:

| Column | Type | Description |
|---------|------|-------------|
| id | INTEGER | Auto-increment primary key |
| product | TEXT | Product name |
| quantity | INTEGER | Quantity sold |
| price | REAL | Price per unit |

---

## ⚙️ Steps Performed
1. Created a SQLite database (`sales_data.db`) and inserted sample sales records.
2. Wrote SQL query to calculate:
   ```sql
   SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue
   FROM sales
   GROUP BY product;
