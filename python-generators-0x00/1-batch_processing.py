#!/usr/bin/python3
import seed


def stream_users_in_batches(batch_size):
    """
    Generator that yields batches of users.
    Uses 'yield' to return each batch of rows.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data;")

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch  # ✅ generator yield here

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """
    Processes batches and yields users over the age of 25.
    Uses yield instead of return for generator compliance.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if int(user["age"]) > 25:
                yield user  # ✅ yield each processed user
