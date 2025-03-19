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
