#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    email TEXT
)
""")

cursor.executemany(
    "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
    [
        ("Alice", 30, "alice@example.com"),
        ("Bob", 45, "bob@example.com"),
        ("Charlie", 50, "charlie@example.com"),
    ]
)
conn.commit()
conn.close()
print("✅ Sample users.db created successfully.")
