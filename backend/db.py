import sqlite3

conn = sqlite3.connect("chats.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_message TEXT,
    bot_response TEXT
)
""")
conn.commit()

def save_chat(user_msg, bot_msg):
    cursor.execute(
        "INSERT INTO chats (user_message, bot_response) VALUES (?, ?)",
        (user_msg, bot_msg)
    )
    conn.commit()
