from fastapi import FastAPI

from config.database import Base, engine
from controllers.model_controller import model_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(model_router, prefix="/models", tags=["models"])


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI MVC Boilerplate!"}
