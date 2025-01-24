from sqlalchemy.orm import sessionmaker, Session
from models.tea import TeaModel, Base
from data.tea_data import teas_list
from config.environment import db_URI
from sqlalchemy import create_engine

engine = create_engine(db_URI)
SessionLocal = sessionmaker(bind=engine)

# This seed file is a separate program that can be used to "seed" our database with some initial data.
try:
    print("Recreating database..")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    print("seeding our database..")
    # Seed teas
    db = SessionLocal()
    db.add_all(teas_list)
    db.commit()
    db.close()

    print("bye 👋")
except Exception as e:
    print(e)
