"""
    Data model to create tables in the DB
"""


from sqlalchemy import Column, Float, Integer, String
from database.database import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(String(255))
    price = Column(Float)
    