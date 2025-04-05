from utils.db_utils import get_connection

def get_customer_profile(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE Customer_ID = ?", (customer_id,))
    row = cursor.fetchone()
    conn.close()
    return row