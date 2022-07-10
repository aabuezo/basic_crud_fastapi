from fastapi import FastAPI
from routers.product import router as prod_router
from models import product as prod_model
from database.database import engine



app = FastAPI()


app.include_router(prod_router)


prod_model.Base.metadata.create_all(engine)
