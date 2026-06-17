import pandas as pd
import sqlite3

def process_file(file_name):
    try:
        df = pd.read_csv(file_name)

        conn = sqlite3.connect("database.db")

        df.to_sql(
            "employee_data",
            conn,
            if_exists="replace",
            index=False
        )

        conn.close()

        print("\nData Successfully Processed!")
        print(df.head())

    except Exception as e:
        print("Error:", e)