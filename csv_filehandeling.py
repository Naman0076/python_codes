# Writing data to a CSV file
import csv
import logging
import configure_logging
 
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    logging.info("Opening and writing a CSV file")
    
    writer.writerow(["Emp_ID", "Name", "Department", "Salary"])
    
    writer.writerows([
        [101, "Alice", "HR", 50000],
        [102, "Bob", "IT", 60000],
        [103, "Charlie", "Finance", 55000]
    ])

logging.info("CSV File written Successfully")


#Reading a CSV file:
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    logging.info("opening CSV file in Read mode")
    
    for row in reader:
        print(row)
logging.info(f"Prinitng row: {row}")

#Appending new data to a CSV file
with open("employees.csv", "a", newline="") as file:
    writer = csv.writer(file)
    logging.info(f"Opening and Appending in the CSV file {file}")
    # Adding new rows
    writer.writerow([104, "David", "Marketing", 52000])
    writer.writerow([105, "Eva", "Sales", 48000])

logging.info(f"Data appended successfully in the CSV fiel {file}")