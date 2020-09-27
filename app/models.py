import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.settings import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    created_at = Column(DateTime, default=datetime.datetime.now)
    hide = Column(Boolean, default=False)
    stock = Column(Integer, default=0)
    expire = Column(DateTime, default=None)

    def __repr__(self):
        return '{} -> {}'.format(self.id, self.name)
