"""
import matplotlib.pyplot as plt

def plot_top_products(product_df, customer_type):
    # You must ensure 'Customer_Type' exists in your product_df or adjust this logic
    filtered_df = product_df[product_df['Customer_Type'] == customer_type]
    
    if filtered_df.empty:
        print(f"No data found for customer type '{customer_type}'")
        return

    top_products = filtered_df['Product_Name'].value_counts().head(5)
    
    plt.figure(figsize=(8, 4))
    top_products.plot(kind='bar', color='skyblue')
    plt.title(f"Top 5 Products for {customer_type}")
    plt.ylabel("Recommendation Count")
    plt.xlabel("Product")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{customer_type}_top5.png")
    plt.show()
"""


""""
import sqlite3

def plot_top_products():
    conn = sqlite3.connect("data/smartcart.db")
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT Customer_Type FROM customer_data_cleaned")
    customer_types = [row[0] for row in cursor.fetchall()]

    print("\n📊 Product Insights by Customer Type:\n")

    for cust_type in customer_types:
        print(f"🔸 Analyzing for Customer Type: {cust_type}\n")

        query = """    """
            SELECT p.Product_ID, p.Category, p.Subcategory, COUNT(*) as purchase_count
            FROM customer_data_cleaned c
            JOIN product_recommendation_data p ON c.Last_Purchased_Product = p.Product_ID
            WHERE c.Customer_Type = ?
            GROUP BY p.Product_ID
            ORDER BY purchase_count DESC
            LIMIT 3
        """         """
        cursor.execute(query, (cust_type,))
        products = cursor.fetchall()

        if not products:
            print("   No product data available for this customer type.\n")
            continue

        for idx, (pid, cat, subcat, count) in enumerate(products, start=1):
            print(f"{idx}. Product ID:")
            print(f"   {pid}\n")

            print(f"   Category:")
            print(f"   {cat}\n")

            print(f"   Subcategory:")
            print(f"   {subcat}\n")

            print(f"   Purchased by this customer type:")
            print(f"   {count} times\n")

            print("   Reason:")
            print("   This product has been purchased frequently by")
            print(f"   {cust_type} customers.")
            print("   It likely reflects strong relevance and preference.\n")

        print("---------------------------------------------------\n")

    conn.close()
"""