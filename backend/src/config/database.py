from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:1234@localhost:5432/tasktracker")

session = sessionmaker(
    autocommit = False,
    autoflush=False,
    bind=engine
)

async def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()