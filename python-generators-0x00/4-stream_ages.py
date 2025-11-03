#!/usr/bin/python3
import seed


def stream_user_ages():
    """Generator that yields ages one by one."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data;")
    for row in cursor:
        yield int(row["age"])
    cursor.close()
    connection.close()


def compute_average_age():
    """Computes average age using generator."""
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1
    if count > 0:
        avg = total / count
        print(f"Average age of users: {avg:.2f}")
    else:
        print("No data available.")
