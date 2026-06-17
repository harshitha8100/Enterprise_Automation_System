from file_processor import process_file
from report_generator import generate_report
from scheduler import start_scheduler
from dashboard import show_dashboard
import threading

print("====================================")
print(" Enterprise Automation System ")
print("====================================")

file_name = input("Enter CSV file name: ")

thread1 = threading.Thread(target=process_file, args=(file_name,))
thread1.start()
thread1.join()

generate_report()
show_dashboard()

start_scheduler()