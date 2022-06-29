from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from core.db import Base


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(350))
    date = Column(DateTime)
    user = Column(Integer, ForeignKey("user.id"))
    user_id = relationship("User")
