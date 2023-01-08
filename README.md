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
This should start the HTTP server on port 5000.

## Endpoints
### 1. Banks
- `GET` /banks - To retrieve list of all banks
- `GET` /banks/{id} - To retrieve bank details of the specified `id`
### 2. Branches
- `GET` /banks/{id}/branches - To retrieve list of all branches for the specified bank `id`
- `GET` /banks/{id}/branches/{ifsc-code} - To retrieve details for a specified branch's IFSC code matching the bank `id`


