from src.config.database import base
from sqlalchemy import Column,String,Integer,DateTime,Boolean,func

class Task(base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True , index=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)