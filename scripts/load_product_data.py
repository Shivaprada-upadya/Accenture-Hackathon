import pandas as pd
from utils.db_utils import get_connection

def load_products():
    df = pd.read_excel("data/product_recommendation_data.csv")
    conn = get_connection()
    df.to_sql("products", conn, if_exists="replace", index=False)
    conn.close()

load_products()