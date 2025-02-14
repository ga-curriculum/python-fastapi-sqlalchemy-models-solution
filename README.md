# FastAPI MVC CRUD Build Solution

## About

This repo contains the solution code for the [Python FastAPI SQLAlchemy Models](https://pages.git.generalassemb.ly/modular-curriculum-all-courses/python-fastapi-sqlalchemy-models/canvas-landing-pages/fallback.html) Lesson.

## Getting Started

1. Fork and clone this repo.

2. Navigate into the project directory:

```sh
 cd python-fastapi-sqlalchemy-models-solution
```

3. Install dependencies (this also creates the virtual environment if it doesn’t exist):

```sh
 pipenv install
```

4. Activate the virtual environment:

```sh
 pipenv shell
```

### Set up the database

1. Set up your PostgreSQL database:

   - Ensure PostgreSQL is installed and running on your machine.
   - Create a database named `teas_db` if it does not already exist:

```bash
createdb teas_db
```

2. Seed the database with initial data:

- Run the `seed.py` file to reset the database by dropping existing tables and repopulating it with starter data:

```bash
pipenv run python seed.py
```

> You should see output indicating the database was successfully seeded. If there are any errors, check the `db_URI` in the `config/environment.py` file.

### Verifying the Data

Once seeding has completed, re-connect to the `psql` shell:

```sh
psql -d teas_db -U <username>
```

In the psql shell, run the following query:

```sql
SELECT * FROM teas;
```

You should see something like the following:

```
| id |       name       | in_stock | rating |
|----|------------------|----------|--------|
|  1 | chai             | t        |      4 |
|  2 | earl grey        | f        |      3 |
|  3 | matcha           | t        |      3 |
|  4 | green tea        | t        |      5 |
|  5 | black tea        | t        |      4 |
|  6 | oolong           | f        |      4 |
|  7 | hibiscus         | t        |      4 |
|  8 | peppermint       | t        |      5 |
|  9 | jasmine          | t        |      3 |
```

## Notes on Configuration

- The database connection string is defined in the `config/environment.py` file:

  ```python
  db_URI = "postgresql://<username>@localhost:5432/teas_db"
  ```

- Ensure your PostgreSQL instance is configured to allow connections with the provided credentials.
- **_Modify your database connection string to use your username as the `<username>`._**

### Setting Up a User in PostgreSQL

To connect to a specific PostgreSQL user, use the following command:

```sh
psql -U <username>
```

#### Handling "Role Does Not Exist" Error

If you see this error:

```sh
Error: FATAL: role "<username>" does not exist
```

it means that the specified user does not exist in PostgreSQL.

#### Creating a New PostgreSQL User

To create the user, run the following command inside `psql`:

```sql
CREATE ROLE "<username>" WITH LOGIN PASSWORD 'your_secure_password';
```

> 🔹 **Replace** `<username>` with your desired username and **choose a secure password**.

This will allow you to connect using one of the following database connection strings:

#### Connection Strings:

If **no password is required**:

```python
db_URI = "postgresql://<username>@localhost:5432/teas_db"
```

If **a password is required**:

```python
db_URI = "postgresql://<username>:<your_secure_password>@localhost:5432/teas_db"
```

This ensures that PostgreSQL correctly authenticates and allows access to the `teas_db` database.
