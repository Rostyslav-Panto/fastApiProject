import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from starlette.staticfiles import StaticFiles

from app.config import settings
from routers.csv_routes import router

load_dotenv('.env')

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)

app.include_router(router)

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
