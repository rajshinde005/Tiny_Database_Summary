# sales_summary.py
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

DB_FILE = "sales_data.db"

# Step 1 — Create DB and table if not exists
def create_database():
    if os.path.exists(DB_FILE):
        print("Database already exists.")
        return

    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    # Create sales table
    cur.execute("""
    CREATE TABLE sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        quantity INTEGER,
        price REAL
    );
    """)

    # Insert sample rows
    data = [
        ("Chocolate", 10, 2.5),
        ("Chocolate", 5, 2.5),
        ("Cookies", 8, 1.75),
        ("Cookies", 7, 1.75),
        ("Candy", 20, 0.5)
    ]
    cur.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", data)

    conn.commit()
    conn.close()
    print("✅ Database created and sample data inserted!")

# Step 2 — Query and plot
def show_summary():
    conn = sqlite3.connect(DB_FILE)

    query = """
    SELECT product,
           SUM(quantity) AS total_qty,
           SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY product;
    """

    df = pd.read_sql_query(query, conn)
    print("\n=== SALES SUMMARY ===")
    print(df)

    df.plot(kind="bar", x="product", y="revenue", legend=False)
    plt.title("Revenue by Product")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("sales_chart.png")
    plt.show()

    conn.close()

if __name__ == "__main__":
    create_database()
    show_summary()
