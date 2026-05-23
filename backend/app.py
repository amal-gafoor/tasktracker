from src.config.database import engine, base
from src.models import schemas
from fastapi import FastAPI
from src.route.task_route import router


app = FastAPI()

app.include_router(router)


@app.on_event("startup")
def on_startup():
    base.metadata.create_all(bind=engine)
    print("Database tables created successfully")
    

@app.get("/")
def root():
    return {"message": "Hello World"}

