#!/usr/bin/python3
import seed


def stream_users_in_batches(batch_size):
    """Generator that yields users in batches."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data;")
    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch
    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """Processes batches and prints users over age 25."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if int(user["age"]) > 25:
                print(user)
