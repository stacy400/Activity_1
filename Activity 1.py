import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="njoga1234",
    database="sample_db"
)

query = "SELECT * FROM sales"

# Load MySQL data into Python (pandas DataFrame)
df = pd.read_sql(query, conn)
print("Extracted Data:")
print(df)

# Transform: Clean / process data
# Example: calculate total sales
df['total_sales'] = df['quantity'] * df['price']

# Sort by total_sales descending
df = df.sort_values(by='total_sales', ascending=False)

print("\nTransformed Data:")
print(df)

# Load: Save transformed data to CSV
df.to_csv("sales_transformed.csv", index=False)
print("\nData loaded to CSV successfully!")
print("sales_transformed.csv")