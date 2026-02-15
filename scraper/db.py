import os
import psycopg2

def get_connection():
    db_url = os.environ["DATABASE_URL"]   # must be this exact line
    return psycopg2.connect(db_url)
