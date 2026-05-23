from src.config.database import engine, base
from src.models import schemas
from fastapi import FastAPI


app = FastAPI()



@app.on_event("startup")
def on_startup():
    base.metadata.create_all(bind=engine)
    print("Database tables created successfully")
    

@app.get("/")
def root():
    return {"message": "Hello World"}

