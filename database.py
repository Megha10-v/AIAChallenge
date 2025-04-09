import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def init_db():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scraped_table (
        id SERIAL PRIMARY KEY,
        data TEXT NOT NULL
    )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()

def store_data(data):
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    cursor = conn.cursor()

    cursor.executemany("INSERT INTO scraped_table (data) VALUES (%s)", data)
    conn.commit()
    
    cursor.close()
    conn.close()

def get_all_news():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    cursor = conn.cursor()

    cursor.execute("SELECT id, data FROM scraped_table")
    articles = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return articles  

def search_news(query):
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    cursor = conn.cursor()

    cursor.execute("SELECT id, data FROM scraped_table WHERE data ILIKE %s", ('%' + query + '%',))
    results = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return results if results else [] 
