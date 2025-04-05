# setup_db.py

import sqlite3
import pandas as pd

# Load CSV data
customer_df = pd.read_csv('data/customer_data_collection.csv')
product_df = pd.read_csv('data/product_recommendation_data.csv')

# Connect to SQLite database (or create it)
conn = sqlite3.connect('smartcart.db')
cursor = conn.cursor()

# Create customers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
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

# Create products table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
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

# Insert CSV data into tables
customer_df.to_sql('customers', conn, if_exists='replace', index=False)
product_df.to_sql('products', conn, if_exists='replace', index=False)

conn.commit()
conn.close()

print("✅ Database created and data loaded successfully.")
