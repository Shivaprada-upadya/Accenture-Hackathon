
# Load CSVs

import sqlite3
import pandas as pd


def get_connection(db_name="smartcart.db"):
    return sqlite3.connect(db_name)
# Load CSVs
customers_df = pd.read_csv('data/customer_data_collection.csv')
products_df = pd.read_csv('data/product_recommendation_data.csv')

# 🔥 Remove unwanted 'Unnamed' columns from both datasets
customers_df = customers_df.loc[:, ~customers_df.columns.str.contains('^Unnamed')]
products_df = products_df.loc[:, ~products_df.columns.str.contains('^Unnamed')]

# Connect to SQLite DB
conn = sqlite3.connect('smartcart.db')
cursor = conn.cursor()

# Drop existing tables if they exist
cursor.execute("DROP TABLE IF EXISTS customers")
cursor.execute("DROP TABLE IF EXISTS products")

# Create the 'customers' table
cursor.execute('''
CREATE TABLE customers (
    Customer_ID TEXT PRIMARY KEY,
    Age INTEGER,
    Gender TEXT,
    Location TEXT,
    Browsing_History TEXT,
    Purchase_History TEXT,
    Customer_Segment TEXT,
    Avg_Order_Value REAL,
    Holiday TEXT,
    Season TEXT
)
''')

# Create the 'products' table
cursor.execute('''
CREATE TABLE products (
    Product_ID TEXT PRIMARY KEY,
    Category TEXT,
    Subcategory TEXT,
    Price REAL,
    Brand TEXT,
    Average_Rating_of_Similar_Products REAL,
    Product_Rating REAL,
    Customer_Review_Sentiment_Score REAL,
    Holiday TEXT,
    Season TEXT,
    Geographical_Location TEXT,
    Similar_Product_List TEXT,
    Probability_of_Recommendation REAL
)
''')

# ✅ Now insert clean data
customers_df.to_sql('customers', conn, if_exists='append', index=False)
products_df.to_sql('products', conn, if_exists='append', index=False)

conn.commit()
conn.close()

print("✅ Cleaned data inserted successfully.")
