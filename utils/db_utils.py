import sqlite3

# Get database connection
def get_connection():
    return sqlite3.connect("smartcart.db")

# Create tables if they don't exist
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Customer Table
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

    # Product Table
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

    conn.commit()
    conn.close()
