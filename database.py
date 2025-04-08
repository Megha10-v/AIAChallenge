import sqlite3

DB_NAME = "ai_news.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        explanation TEXT
    )
    """)
    conn.commit()
    conn.close()

def store_data(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.executemany("INSERT INTO news (explanation) VALUES (?)", data)
    conn.commit()
    conn.close()

def get_all_news():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, explanation FROM news")
    articles = [{"id": row[0], "explanation": row[1]} for row in cursor.fetchall()]
    conn.close()

    return articles

def search_news(query):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT id, explanation FROM news WHERE explanation LIKE ?", ('%' + query + '%',))
    results = [{"id": row[0], "explanation": row[1]} for row in cursor.fetchall()]
    conn.close()

    return results
