from pydantic import BaseModel


class ModelBase(BaseModel):
    id: int
    name: str
    description: str


class ModelCreate(ModelBase):
    pass


class ModelResponse(ModelBase):
    class Config:
        orm_mode = True
