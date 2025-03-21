import json
#Writing in Json file
# Sample employee data
data = {
    "employees": [
        {"Emp_ID": 101, "Name": "Alice Johnson", "Department": "HR", "Salary": 50000, "Email": "alice.johnson@example.com"},
        {"Emp_ID": 102, "Name": "Bob Smith", "Department": "IT", "Salary": 60000, "Email": "bob.smith@example.com"},
        {"Emp_ID": 103, "Name": "Charlie Brown", "Department": "Finance", "Salary": 55000, "Email": "charlie.brown@example.com"},
        {"Emp_ID": 104, "Name": "David Wilson", "Department": "Marketing", "Salary": 52000, "Email": "david.wilson@example.com"},
        {"Emp_ID": 105, "Name": "Eva Adams", "Department": "Sales", "Salary": 48000, "Email": "eva.adams@example.com"}
    ]
}
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file created successfully!")
############################################

# Reading JSON data from the file
with open("data.json", "r") as file:
    data = json.load(file)
print(json.dumps(data, indent=4))  

############################################

# Search for employee with ID 103
def find_employee(emp_id):
    with open("data.json", "r") as file:
        data = json.load(file)

    for emp in data["employees"]:
        if emp["Emp_ID"] == emp_id:
            return emp
    return None

emp_id = 103
employee = find_employee(emp_id)

if employee:
    print(f"Employee Found: {employee}")
else:
    print(f"!!Employee with ID {emp_id} not found.!!")

####################################################
# Update salary of employee with ID 102
def update_salary(emp_id, new_salary):
    with open("data.json", "r") as file:
        data = json.load(file)

    for emp in data["employees"]:
        if emp["Emp_ID"] == emp_id:
            emp["Salary"] = new_salary
            break
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    print(f"Salary updated for Employee ID {emp_id}")

update_salary(102, 65000)

####################################################
# Adding a new employee
def add_employee(new_employee):
    with open("data.json", "r") as file:
        data = json.load(file)

    data["employees"].append(new_employee)
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("New employee added successfully!")


new_employee = {
    "Emp_ID": 106,
    "Name": "Frank Miller",
    "Department": "IT",
    "Salary": 65000,
    "Email": "frank.miller@example.com"
}
add_employee(new_employee)

##################################################
# Delete employee with ID 104
def delete_employee(emp_id):
    with open("data.json", "r") as file:
        data = json.load(file)

    data["employees"] = [emp for emp in data["employees"] if emp["Emp_ID"] != emp_id]

    # Writing updated data back to file
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    print(f"!Employee with ID {emp_id} deleted successfully!")


delete_employee(104)
