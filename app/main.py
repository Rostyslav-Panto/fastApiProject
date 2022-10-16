from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from routers.csv_routes import router

app = FastAPI()
app.include_router(router)
app.mount("/static", StaticFiles(directory="static"), name="static")
