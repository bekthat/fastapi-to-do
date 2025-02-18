from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal, engine, Base
from ..import schemas, crud

Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/todos", response_model=list[schemas.ToDoResponse])
def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)

@router.post("/todos", response_model=schemas.ToDoResponse)
def create_todo(todo: schemas.ToDoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    return crud.delete_todo(db, todo_id)
