import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.settings import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    created_at = Column(DateTime, default=datetime.datetime.now)

    @staticmethod
    def exists(session, **kwargs):
        r = session.query(Product).filter_by(**kwargs).first()
        return r is not None
    
    def __repr__(self):
        return '{} -> {}'.format(self.id, self.name)

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    created_at = Column(DateTime, default=datetime.datetime.now)
  