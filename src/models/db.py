from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

Session = sessionmaker(bind=engine)

Base = declarative_base()