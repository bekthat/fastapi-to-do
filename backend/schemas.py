from pydantic import BaseModel

class ToDoBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False  # Добавляем поле

class ToDoCreate(ToDoBase):
    pass

class ToDoUpdate(ToDoBase):
    pass

class ToDoInDB(ToDoBase):
    id: int

    class Config:
        orm_mode = True
