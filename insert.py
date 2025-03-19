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
