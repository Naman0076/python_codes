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