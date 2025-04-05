# agents/customer_agent.py

from utils.db_utils import get_connection

def get_customer_profile(customer_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM customers WHERE Customer_ID = ?"
    cursor.execute(query, (customer_id,))
    result = cursor.fetchone()

    conn.close()

    if result:
        columns = [description[0] for description in cursor.description]
        profile = dict(zip(columns, result))
        return profile
    else:
        return None
