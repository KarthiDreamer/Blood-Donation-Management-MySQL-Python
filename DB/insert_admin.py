import mysql.connector

## insert in hospital table first lol

database_name = 'autogenerated_blood_donation'

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yh1pwth@t",
    # database=database_name
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

cursor.execute("USE autogenerated_blood_donation;")

admin_data = [
    ('dhanesh',1234, 'Pbks2023Cup'),
    ('karthi',5678, 'K@rth1rOcks')
]

admin_data_insert_query = """
    INSERT INTO admin (admin_name, admin_id, password)
    VALUES (           %s        ,%s       ,%s);
"""

cursor.executemany(admin_data_insert_query,admin_data)

conn.commit()

print("Admin data inserted successfully!")

# Close the cursor and the connection
cursor.close()
conn.close()