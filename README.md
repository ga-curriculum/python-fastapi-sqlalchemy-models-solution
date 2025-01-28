# FastAPI MVC CRUD Build Solution

## About

This repo contains the solution code for the [Python FastAPI SQLAlchemy Models](https://pages.git.generalassemb.ly/modular-curriculum-all-courses/python-fastapi-sqlalchemy-models/canvas-landing-pages/fallback.html) Lesson.

## Getting Started

1. Fork and clone this repo to your local machine.

2. Navigate to the project directory and activate the virtual environment:

   ```bash
   pipenv shell
   ```

3. Install the dependencies:

   ```bash
   pipenv install
   ```

4. Set up your PostgreSQL database:

   - Ensure PostgreSQL is installed and running on your machine.
   - Create a database named `teas_db`:

     ```bash
     createdb teas_db
     ```

5. Seed the database with initial data:

   - Run the `seed.py` file to populate the database with data:

     ```bash
     pipenv run python seed.py
     ```

   You should see output indicating the database was successfully seeded. If there are any errors, check the `db_URI` in the `config/environment.py` file.

6. Start the development server:

   ```bash
   pipenv run uvicorn main:app --reload
   ```

7. Open the application in Visual Studio Code:

   ```bash
   code .
   ```

### Notes on Configuration

- The database connection string is defined in the `config/environment.py` file:

  ```python
  db_URI = "postgresql://postgres:postgres@localhost:5432/teas_db"
  ```

- Ensure your PostgreSQL instance is configured to allow connections with the provided credentials.