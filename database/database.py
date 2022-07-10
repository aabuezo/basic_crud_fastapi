"""
    This file creates the database connection wiht MySQL
    You can install MySQL locally or run it with Docker
    date: june 27, 
    database should be created forehand
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.get_data import get_db_data

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
data = get_db_data()
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{data['user']}:{data['password']}@{data['host']}/{data['database']}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
