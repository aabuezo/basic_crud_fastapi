"""
    This file creates and manage the routes to /product endpoint
"""

from curses.ascii import HT
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from schemas import product as prod_schema
from typing import List
from models import product as prod_model
from database.database import get_db


router = APIRouter()


@router.post('/product', status_code=status.HTTP_201_CREATED)
async def add_product(request: prod_schema.Product, db: Session = Depends(get_db)):
    new_product = prod_model.Product(
        name=request.name, 
        description=request.description, 
        price=request.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request


@router.get('/product/{id}', response_model=prod_schema.ResponseProduct)
async def get_product(id: int, response: Response, db: Session = Depends(get_db)):
    product = db.query(prod_model.Product).filter(prod_model.Product.id==id).first()
    if not product:
        # response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='product not found')
    return product


@router.get('/products', response_model=List[prod_schema.ResponseProduct])
async def get_all_products(db: Session = Depends(get_db)):
    product_list = db.query(prod_model.Product).all()
    return product_list


@router.delete('/product/{id}')
async def delete_product(id: int, db: Session = Depends(get_db)):
    db.query(prod_model.Product).filter(prod_model.Product.id==id).delete(synchronize_session=False)
    db.commit()
    return {'message': 'product deleted'}


@router.put('/product/{id}')
async def update_product(request: prod_schema.Product, id: int, db: Session = Depends(get_db)):
    product = db.query(prod_model.Product).filter(prod_model.Product.id==id)
    if not product.first():
        return {'error': f'product {id} does not exist.'}
    product.update(request.dict())
    db.commit()
    return {'message': 'product successfully updated'}
