from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from schemas import TaskCreate, TaskUpdate, TaskResponse
from crud import TaskCRUD
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Task
@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return TaskCRUD.create_task(db, task)

# Read All Tasks
@app.get("/tasks", response_model=list[TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return TaskCRUD.get_all_tasks(db)

# Read Single Task
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = TaskCRUD.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update Task
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, update_data: TaskUpdate, db: Session = Depends(get_db)):
    task = TaskCRUD.update_task_done(db, task_id, update_data)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Delete Task
@app.delete("/tasks/{task_id}", response_model=TaskResponse)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = TaskCRUD.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
if __name__ == "__main__":
    import  uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8069, reload=True)


