from sqlalchemy.orm import Session
from . import models
from . import schemas


def get_todos(db: Session):
    return db.query(models.ToDo).all()

def create_todo(db: Session, todo: schemas.ToDoCreate):
    db_todo = models.ToDo(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo

def update_todo(db: Session, todo_id: int, todo_update: schemas.ToDoUpdate):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if db_todo:
        db_todo.title = todo_update.title
        db_todo.description = todo_update.description
        db_todo.completed = todo_update.completed
        db.commit()
        db.refresh(db_todo)
    return db_todo