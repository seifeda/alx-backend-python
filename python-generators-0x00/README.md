# alx-backend-python# Python Generators Project

This project demonstrates the use of Python **generators** to handle large datasets efficiently, especially when working with databases.

---

## Tasks

### 0. Getting started with Python Generators

- **Goal**: Connect to MySQL and populate the `ALX_prodev.user_data` table.
- **File**: `seed.py`
- Functions:
  - `connect_db()`
  - `create_database(connection)`
  - `connect_to_prodev()`
  - `create_table(connection)`
  - `insert_data(connection, data)`

---

### 1. Stream users one by one

- **Goal**: Use a generator to stream rows one by one.
- **File**: `0-stream_users.py`
- Function: `stream_users()`

---

### 2. Batch Processing

- **Goal**: Fetch and process data in batches.
- **File**: `1-batch_processing.py`
- Functions:
  - `stream_users_in_batches(batch_size)`
  - `batch_processing(batch_size)`

---

### 3. Lazy Pagination

- **Goal**: Simulate paginated data fetching using lazy loading.
- **File**: `2-lazy_paginate.py`
- Functions:
  - `paginate_users(page_size, offset)`
  - `lazy_pagination(page_size)`

---

### 4. Memory-Efficient Aggregation

- **Goal**: Calculate average user age using generators.
- **File**: `4-stream_ages.py`
- Functions:
  - `stream_user_ages()`
  - `compute_average_age()`

---

## Requirements

- Python 3.8+
- MySQL Server
- `mysql-connector-python` library

Install dependencies:

```bash
pip install mysql-connector-python
```
