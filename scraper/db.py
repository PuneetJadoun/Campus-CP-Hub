import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # loads .env file

def get_connection():
    db_url = os.environ["DATABASE_URL"]
    return psycopg2.connect(db_url)
