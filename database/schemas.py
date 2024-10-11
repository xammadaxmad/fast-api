from pydantic import BaseModel

class CreateTask(BaseModel):
    name:str
    desc:str = None