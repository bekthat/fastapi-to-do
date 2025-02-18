from pydantic import BaseModel

class ToDoBase(BaseModel):
    title: str
    description: str | None = None

class ToDoCreate(ToDoBase):
    pass

class ToDoResponse(ToDoBase):
    id: int

    class Config:
        orm_mode = True
