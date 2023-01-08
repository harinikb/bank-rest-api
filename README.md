# Banks REST API
REST API server to retrieve banks and branches with Flask, PostgreSQL.

## Pre-requisites
- Python 3.11
- pip 22.3.1
- PostgreSQL 15

## Setup
1. To install python dependencies
```bash
$ pip install -r requirements.txt
```

2. Creating Database in PostgreSQL. Connect to PostgreSQL instance and create `banks_dump` database.
```
# CREATE DATABASE banks_dump;
```

3. To create tables associated tables
```bash
$ psql -U <user_name> -d banks_dump -f .\database\tables.sql
```

4. To seed data into the database instance
```bash
$ psql -U postgres -d banks_dump -f .\database\banks.sql
$ psql -U postgres -d banks_dump -f .\database\branches.sql
```
5. To start the HTTP server
```bash
$ python run.py
```

