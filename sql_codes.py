import pymysql 
import os
from dotenv import load_dotenv
load_dotenv()
# Open database connection 
connection = pymysql.connect(
    host=os.getenv('host'),
    user=os.getenv('user'),  # Change to your actual MySQL username
    password=os.getenv('password'),  # Change to your actual password
    db=os.getenv('db')  # Change to your actual database name
)

# Create a cursor object 
cursor = connection.cursor() 

# Execute SQL query to fetch all employees
cursor.execute("SELECT * FROM employee;")
rows = cursor.fetchall()
for row in rows: 
    print(row)

# ✅ Insert Employee Data (Emp_NO 9 & 10)
sql_insert_query = """
INSERT INTO employee (Emp_NO, Emp_Name, Emp_Add, Emp_Phone, Dept_No, Dept_Name, Salary, Job_ID) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

# Employee data for Emp_NO 9 & 10
employee_data = [
    (90, "Harshit", "Hauz Khas", "9855498465", 7600, "Development", 10000, 7006),
    (100, "Hari", "Noida", "9988776655", 7600, "Development", 11000, 7011),
]

# Execute the insertion query
cursor.executemany(sql_insert_query, employee_data)
connection.commit()
print("✅ Employee 9 & 10 inserted successfully!")

# ✅ Update Employee 9 (Harshit)
sql_update_query = """
UPDATE employee 
SET Emp_Name = %s, Emp_Add = %s, Emp_Phone = %s, Dept_No = %s, Dept_Name = %s, Salary = %s, Job_ID = %s 
WHERE Emp_NO = %s
"""

# Updated details for Emp_NO 9
updated_data = ("Harshit Sharma", "New Delhi", "9876543210", 7600, "Tech Support", 15000, 7012, 9)

# Execute the update query
cursor.execute(sql_update_query, updated_data)
connection.commit()
print("✅ Employee 9 (Harshit) updated successfully!")

# ✅ Delete Employee 10 (Hari)
sql_delete_query = "DELETE FROM employee WHERE Emp_NO = %s"
emp_no_to_delete = (10,)

cursor.execute(sql_delete_query, emp_no_to_delete)
connection.commit()
print("✅ Employee 10 (Hari) deleted successfully!")

# Close the cursor and the connection
cursor.close()
connection.close()
