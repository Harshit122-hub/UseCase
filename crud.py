from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskUpdate

class TaskCRUD:

    @staticmethod
    def create_task(db: Session, task_data: TaskCreate):
        print('TaskCreate',TaskCreate)
        task = Task(**task_data.dict())
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    @staticmethod
    def get_task(db: Session, task_id: int):
        return db.query(Task).filter(Task.id == task_id).first()

    @staticmethod
    def get_all_tasks(db: Session):
        return db.query(Task).all()

    @staticmethod
    def update_task(db: Session, task_id: int, update_data: TaskUpdate):
        task = db.query(Task).filter(Task.id == task_id).first()
        if task:
            update_fields = update_data.dict(exclude_unset=True)
            for key, value in update_fields.items():
                setattr(task, key, value)

            db.commit()
            db.refresh(task)
        return task
        
        return None


    @staticmethod
    def delete_task(db: Session, task_id: int):
        task = db.query(Task).filter(Task.id == task_id).first()
        if task:
            db.delete(task)
            db.commit()
        return task
