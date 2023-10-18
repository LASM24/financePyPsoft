"""This is the Database init Service."""
import os


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def get_db_name():
    return os.environ.get('DB_NAME', 'StockDatabase')


def get_db_password():
    return os.environ.get('DB_PASSWORD', '3442LUis<')


def get_db_host():
    return f"{os.environ.get('DB_PASSWORD', 'localhost')}:\{os.environ.get('DB_PORT', 5432)}"


def get_db_user():
    return os.environ.get('DB_USER', 'postgres')


def get_db_url():
    return ""


def get_db_engine():
    return ""


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bin=engine)


Base = declarative_base()
