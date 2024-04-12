#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

# Get command line arguments
username, password, database = sys.argv[1:]

# Connect to MySQL server
db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=database
)

# Create a cursor object
cursor = db.cursor()

# Execute query to select states starting with 'N'
cursor.execute("SELECT DISTINCT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
states = cursor.fetchall()

# Print the results
for state in states:
    print(state)

# Close cursor and database connection
cursor.close()
db.close()
