from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import database

app = FastAPI()


@app.get("/")
def index(db:Session = Depends(database.get_db)):
    print(db)
    return "Hello World"
