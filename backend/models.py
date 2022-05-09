from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)