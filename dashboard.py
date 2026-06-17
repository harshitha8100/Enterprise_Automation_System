import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def show_dashboard():
    try:
        conn = sqlite3.connect("database.db")

        df = pd.read_sql_query(
            "SELECT * FROM employee_data",
            conn
        )

        conn.close()

        print("\nDashboard Statistics")
        print(df.describe())

        if len(df.columns) >= 2:
            column = df.columns[1]

            if pd.api.types.is_numeric_dtype(df[column]):
                plt.figure(figsize=(8,5))
                plt.hist(df[column], bins=10)
                plt.title("Analytics Dashboard")
                plt.xlabel(column)
                plt.ylabel("Frequency")
                plt.show()

    except Exception as e:
        print("Dashboard Error:", e)