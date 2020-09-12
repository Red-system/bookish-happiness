import sys
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sys.dont_write_bytecode = True

engine = create_engine(
    "mysql+mysqldb://root:@localhost/frigo",
    pool_recycle=3600
)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
