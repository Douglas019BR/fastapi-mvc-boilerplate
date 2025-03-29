from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import get_db
from models.model import Model
from schemas.model_schema import ModelCreate, ModelResponse

model_router = APIRouter()


@model_router.post("/", response_model=ModelResponse)
def create_model(model_data: ModelCreate, db: Session = Depends(get_db)):
    some_validation = False
    if some_validation:
        raise Exception("some validation Error")
    new_model = Model(**model_data.dict())
    db.add(new_model)
    db.commit()
    db.refresh(new_model)
    return new_model


@model_router.get("/{model_id}", response_model=ModelResponse)
def get_model(model_id: int, db: Session = Depends(get_db)):
    db_model = db.query(Model).filter(Model.id == model_id).first()
    if not db_model:
        raise HTTPException(status_code=404, detail="Model not found.")
    return db_model
