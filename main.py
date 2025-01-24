from fastapi import FastAPI
# Let's import some of the SQLAlchemy libraries that we'll need
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
# Let's also import the database uri, which will point to our teas_db
from config.environment import db_URI
from controllers.teas import router as TeasRouter
from database import get_db  # import get_db from database.py

app = FastAPI()

app.include_router(TeasRouter, prefix="/api")


@app.get('/')
def home():
    return 'Hello World!'
