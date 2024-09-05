import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('test.db')
conn.row_factory = sqlite3.Row  # Access rows by column names

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a query
cursor.execute('SELECT * FROM company')

# Fetch all rows as a list of dictionaries
rows = cursor.fetchall()

# Convert rows to a list of dictionaries
users_list = []
for row in rows:
    user = dict(row)  # Convert Row object to dictionary
    users_list.append(user)

# Print the list of dictionaries
print(users_list)

# Close cursor and connection
cursor.close()
conn.close()
