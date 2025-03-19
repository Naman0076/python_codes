import pymysql 
# Open database connection 
connection = pymysql.connect(host='localhost', user='root', password='Ncky@0719', db='flask')
# Create a cursor object 
cursor = connection.cursor() 

# Execute SQL query 
cursor.execute("SELECT * FROM employee;")

# Fetch all rows 
rows = cursor.fetchall()
 
for row in rows: 
    print(row)
# Close database connection 
connection.close()

######################################################

import pymysql

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='root',  # Change to your actual MySQL username
    password='Ncky@0719',  # Change to your actual password
    db='flask'  # Change to your actual database name
)

# Cursor object creation
cursor = connection.cursor()

# Define the SQL query for inserting into the employee table
sql_query = """
INSERT INTO employee (Emp_NO, Emp_Name, Emp_Add, Emp_Phone, Dept_No, Dept_Name, Salary, Job_ID) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

# Employee data from the table
employee_data = [
    (8, "Naman", "Hauz Khas", "9855498465", 7600, "Developement", 10000, 7006),
]

# Execute the query with all employee data
cursor.executemany(sql_query, employee_data)

# Commit the changes
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()

print("Employee data inserted successfully!")

######################################################
import pymysql

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='root',  # Change to your actual MySQL username
    password='Ncky@0719',  # Change to your actual password
    db='flask'  # Change to your actual database name
)

# Cursor object creation
cursor = connection.cursor()

# Define the SQL query for updating Naman Kaushik's details
sql_update_query = """
UPDATE employee 
SET Emp_Name = %s, Emp_Add = %s, Emp_Phone = %s, Dept_No = %s, Dept_Name = %s, Salary = %s, Job_ID = %s 
WHERE Emp_NO = %s
"""

# Updated details for Naman Kaushik (Emp_NO 8)
updated_data = ("Naman Kaushik", "South Delhi", "9999888877", 7600, "Development", 12000, 7010, 8)

# Execute the update query
cursor.execute(sql_update_query, updated_data)

# Commit the changes
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()

print("Naman Kaushik's data updated successfully!")

######################################################

import pymysql

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='root',  # Change to your actual MySQL username
    password='Ncky@0719',  # Change to your actual password
    db='flask'  # Change to your actual database name
)

# Cursor object creation
cursor = connection.cursor()

# Define the SQL query to delete Naman Kaushik's record
sql_delete_query = """
DELETE FROM employee WHERE Emp_NO = %s
"""

# Employee number to delete (Emp_NO 8)
emp_no_to_delete = (8,)

# Execute the delete query
cursor.execute(sql_delete_query, emp_no_to_delete)

# Commit the changes
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()

print(" Naman Kaushik's record deleted successfully!")
