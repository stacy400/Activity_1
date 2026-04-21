import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="njoga1234",
    database="sample_db"
)

# Query data
query = "SELECT * FROM sales"

df = pd.read_sql(query, conn)

print("Extracted Data:")
print(df)