from fastapi import APIRouter, Request
from typing import List

from starlette.templating import Jinja2Templates

from schemas.People import People

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/")
def main(request: Request):
    csv = ["First CSV",
           "Second CSV",
           "Third CSV",
           "Fourth CSV",
           "Fifth CSV",
           "Sixth CSV"]
    return templates.TemplateResponse("index.html", {"request": request, "csv": csv})


@router.post("/fetch_csv/")
def fetch_csv(people: List[People]):
    print(people)
    return


@router.get("/csv/{csv_name}")
def get_csv_data(request: Request, csv_name: str):
    return templates.TemplateResponse("csv_data.html", {"request": request, "csv_name": csv_name})
