# Setup

1. Creating Database in PostgreSQL. Connect to PostgreSQL instance and create `banks_dump` database.
```
# CREATE DATABASE banks_dump;
```

2. To create tables associated tables
```bash
$ psql -U <user_name> -d banks_dump -f .\database\tables.sql
```

3. To seed data into the database instance
```bash
$ psql -U postgres -d banks_dump -f .\database\banks.sql
$ psql -U postgres -d banks_dump -f .\database\branches.sql

```

