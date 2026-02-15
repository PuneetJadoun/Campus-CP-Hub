import os
import psycopg2

def get_connection():
    db_url = os.environ.get("DATABASE_URL")
    return psycopg2.connect(db_url)
