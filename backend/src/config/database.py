from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://postgres:1234@localhost:5432/tasktracker")

session = sessionmaker(
    autocommit = False,
    autoflush=False,
    bind=engine
)

base = declarative_base()

async def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()