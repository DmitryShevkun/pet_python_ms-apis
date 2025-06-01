from config import service_db, service_db_write

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
    
# Function to insert a new user
def insert_user(name, email, age):
    query = """
    INSERT INTO users (name, email, age)
    VALUES (%s, %s, %s)
    RETURNING id;
    """
    conn = connect_to_db()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute(query, (name, email, age))
                user_id = cur.fetchone()[0]  # Fetch the returned id
                conn.commit()
                print(f"User inserted with ID: {user_id}")
                return user_id
        except Exception as e:
            print(f"Error inserting user: {e}")
        finally:
            conn.close()