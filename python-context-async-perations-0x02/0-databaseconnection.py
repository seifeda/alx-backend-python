#!/usr/bin/env python3
import sqlite3

class DatabaseConnection:
    """Custom context manager for handling database connections."""
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        """Open the database connection and return the cursor."""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        print("[INFO] Database connection opened.")
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the connection automatically."""
        if self.conn:
            if exc_type:
                print(f"[ERROR] Exception occurred: {exc_val}")
            self.conn.close()
            print("[INFO] Database connection closed.")


if __name__ == "__main__":
    with DatabaseConnection("users.db") as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        print("[RESULT]", results)
