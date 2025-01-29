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

1. Start the development server:

```bash
pipenv run uvicorn main:app --reload
```

> You should now have the app running. Visit [`http://127.0.0.1:8000`](http://127.0.0.1:8000) in your browser to confirm it’s working.

4. Open the application in Visual Studio Code:

```bash
code .
```

### Notes on Configuration

- The database connection string is defined in the `config/environment.py` file:

  ```python
  db_URI = "postgresql://postgres:postgres@localhost:5432/teas_db"
  ```

- Ensure your PostgreSQL instance is configured to allow connections with the provided credentials.
