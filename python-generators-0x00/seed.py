#!/usr/bin/python3
import mysql.connector
import csv
import uuid


def connect_db():
    """Connects to MySQL server (no specific DB yet)."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_database(connection):
    """Creates database ALX_prodev if it does not exist."""
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
    connection.commit()
    cursor.close()


def connect_to_prodev():
    """Connects to ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_table(connection):
    """Creates user_data table if not exists."""
    query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id VARCHAR(50) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL,
        INDEX (user_id)
    );
    """
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    print("Table user_data created successfully")


def insert_data(connection, csv_file):
    """Inserts data into user_data table from CSV if not exists."""
    cursor = connection.cursor()
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            user_id = row.get('user_id') or str(uuid.uuid4())
            name = row['name']
            email = row['email']
            age = row['age']
            cursor.execute(
                "SELECT * FROM user_data WHERE email = %s",
                (email,)
            )
            if cursor.fetchone() is None:
                cursor.execute(
                    "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                    (user_id, name, email, age)
                )
    connection.commit()
    cursor.close()
