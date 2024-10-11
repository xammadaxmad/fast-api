from sqlalchemy import Column, Integer, String
from .connection import Base

class Task(Base):
    __tablename__="tasks"
    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String(255),nullable=True)
    desc = Column(String(255),nullable=True)
    status = Column(String(10),nullable=True)