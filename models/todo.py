from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from db.connection import Base

class ToDo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, default=None)
    completed = Column(String, default="Pending")
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())