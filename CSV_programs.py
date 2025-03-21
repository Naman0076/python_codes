# Writing data to a CSV file
import csv
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow(["Emp_ID", "Name", "Department", "Salary"])
    
    writer.writerows([
        [101, "Alice", "HR", 50000],
        [102, "Bob", "IT", 60000],
        [103, "Charlie", "Finance", 55000]
    ])

print("CSV file written successfully!")


#Reading a CSV file:
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)


#Appending new data to a CSV file
with open("employees.csv", "a", newline="") as file:
    writer = csv.writer(file)
    
    # Adding new rows
    writer.writerow([104, "David", "Marketing", 52000])
    writer.writerow([105, "Eva", "Sales", 48000])

print("Data appended to CSV successfully!")