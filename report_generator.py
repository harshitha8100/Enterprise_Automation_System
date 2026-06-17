import sqlite3

def generate_report():
    try:
        conn = sqlite3.connect("database.db")

        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM employee_data"
        )

        total = cursor.fetchone()[0]

        report = f"""
Enterprise Automation Report
============================
Total Records : {total}
"""

        with open(
            "reports/report.txt",
            "w"
        ) as file:
            file.write(report)

        conn.close()

        print("\nReport Generated Successfully!")

    except Exception as e:
        print("Report Error:", e)