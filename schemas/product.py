"""
    pydantic model to validate request bodies
"""

from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: float


class ResponseProduct(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True
