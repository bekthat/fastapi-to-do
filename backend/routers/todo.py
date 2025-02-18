from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal, engine, Base
from .. import schemas, crud, database

Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/todos", response_model=list[schemas.ToDoInDB])

def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)

@router.post("/todos", response_model=list[schemas.ToDoInDB])
def create_todo(todo: schemas.ToDoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)

@router.put("/todos/{todo_id}", response_model=schemas.ToDoInDB)
def update_todo(todo_id: int, todo_update: schemas.ToDoUpdate, db: Session = Depends(database.get_db)):
    updated_todo = crud.update_todo(db, todo_id, todo_update)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return updated_todo
