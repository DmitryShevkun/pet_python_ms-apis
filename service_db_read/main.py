from config import service_db, service_db_read

import psycopg2
from psycopg2 import sql

# Database connection configuration
DB_CONFIG = {
    "dbname": service_db["dbname"],
    "user": service_db["user"],
    "password": service_db["password"],
    "host": service_db["host"],
    "port": service_db["port"]
}

# Function to connect to the database
def connect_to_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Connected to the database!")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None