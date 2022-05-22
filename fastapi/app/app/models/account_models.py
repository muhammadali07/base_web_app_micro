from datetime import datetime
import email
from typing import Collection
from venv import create

from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey, Date, DateTime, Numeric, Boolean, Float, Identity
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db import Base


class RequestUser(Base):
    __tablename__ = "user_account"
    id = Column(BigInteger,primary_key = True, index = True, autoincrement = True)
    db_id = Column(String(36))
    email = Column(String(200))
    username = Column(String(100))
    password = Column(String(100))
    role = Column(String(20))
    create_at = Column(DateTime, server_default=func.now())

