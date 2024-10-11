from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from database import connection, models,schemas
from helper import response_helper

app = FastAPI()



@app.get("/")
def index():
    return {"status": "success", "message": "Server is running"}


@app.get("/task")
def get_task_list(db: Session = Depends(connection.get_db)):
    data = db.query(models.Task).all()
    arr_return = []
    for dt in data:
        obj = {
            "id": dt.id,
            "name": dt.name,
            "desc": dt.desc,
            "status": dt.status
        }
        arr_return.append(obj)
        
    return response_helper.success("",arr_return)


@app.post("/task")
async def create_task(params:schemas.CreateTask,req:Request, db:Session = Depends(connection.get_db)):
    try:
        task = models.Task()
        task.name = params.name
        task.desc = params.desc
        task.status = "Pending"
        db.add(task)
        db.commit()
        return response_helper.success("Task has been created")
    except Exception as ex:
        message = str(ex)
        return response_helper.error(message)


@app.put("/task/{task_id}")
def update_task():
    pass


@app.delete("/task/{task_id}")
def delete_task():
    pass
