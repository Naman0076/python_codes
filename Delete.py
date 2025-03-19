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
