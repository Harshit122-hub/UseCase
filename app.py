from fastapi import FastAPI ,Request ,Depends
from database import SessionLocal, engine, Base
from sqlalchemy.orm import Session
from crud import TaskCRUD
from schemas import TaskCreate, TaskUpdate, TaskResponse
import models
from fastapi.responses import JSONResponse


# Create tables based on models
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def root():
    return {"message": "DB connection setup complete"}

@app.get("/tasks")
async def root(db: Session = Depends(get_db)):
   return TaskCRUD.get_all_tasks(db)

# Create Task
@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return TaskCRUD.create_task(db, task)

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = TaskCRUD.get_task(db, task_id)
    if not task:
        return JSONResponse(
            status_code=404,
            content={
                "status": "error",
                "message": "Task not found"
            }
        )
    return task

# Update Task
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, update_data: TaskUpdate, db: Session = Depends(get_db)):
    task = TaskCRUD.update_task(db, task_id, update_data)
    if not task:
         return JSONResponse(
            status_code=404,
            content={
                "status": "error",
                "message": "Task not found"
            }
        )
    return task

@app.delete("/tasks/{task_id}", response_model=TaskResponse)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = TaskCRUD.delete_task(db, task_id)
    if not task:
         return JSONResponse(
            status_code=404,
            content={
                "status": "error",
                "message": "Task not found"
            }
        )
    return task

