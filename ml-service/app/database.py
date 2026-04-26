# import sqlite3
# from pathlib import Path

# # Database path
# DB_PATH = Path(__file__).parent.parent / "users.db"

# def init_db():
#     """Initialize SQLite database with users table"""
#     conn = sqlite3.connect(str(DB_PATH))
#     cursor = conn.cursor()
    
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             email TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL,
#             full_name TEXT,
#             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#         )
#     ''')
    
#     conn.commit()
#     conn.close()

# def get_db():
#     """Get database connection"""
#     return sqlite3.connect(str(DB_PATH))

# # Initialize database on import
# init_db()
