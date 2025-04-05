import pandas as pd
from utils.db_utils import get_connection

def load_customers():
    df = pd.read_excel("data/customer_data_collection.csv")
    conn = get_connection()
    df.to_sql("customers", conn, if_exists="replace", index=False)
    conn.close()

load_customers()