import sqlite3
import pandas as pd
from utils.db_utils import get_connection

def get_all_products():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM products", conn)
    conn.close()
    return df
