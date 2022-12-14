import datetime
import petl as etl
from fastapi import APIRouter, Request
from typing import List

from fastapi_sqlalchemy import db
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from schemas.People import People

from app.csv_meta import CSVMeta as ModelCSVMeta
import uuid

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/")
def main(request: Request):
    csv_meta = db.session.query(ModelCSVMeta).all()
    return templates.TemplateResponse("main.html", {"request": request, "csv": csv_meta})


@router.post("/fetch_csv/")
def fetch_csv(people: List[People]):
    new_filename = str(uuid.uuid4()) + '.csv'
    table1 = etl.fromdicts([i.dict() for i in people])
    etl.tocsv(table1, f"csv_data/{new_filename}")

    db_csv_meta = ModelCSVMeta(filename=new_filename)
    db.session.add(db_csv_meta)
    db.session.commit()
    return


@router.get("/csv/{csv_name}")
def get_csv_data(request: Request, csv_name: str):
    table1 = etl.fromcsv(f"csv_data/{csv_name}")
    return templates.TemplateResponse("csv_data.html", {"request": request,
                                                        "csv_name": csv_name,
                                                        "csv_head": etl.header(table1),
                                                        "csv_data": etl.data(table1)
                                                        })


@router.api_route("/csv/{csv_name}/count/", methods=['GET', 'POST'], response_class=HTMLResponse)
def count_csv_data(request: Request, csv_name: str, fields: List[str]=("name",)):
    initial_data = etl.fromcsv(f"csv_data/{csv_name}")
    counted_data = etl.valuecounts(initial_data, *fields)

    counted_data = etl.cutout(counted_data, 'frequency')
    return templates.TemplateResponse("value_count.html", {"request": request,
                                                           "csv_name": csv_name,
                                                           "csv_all_head": etl.header(initial_data),
                                                           "csv_head": etl.header(counted_data),
                                                           "csv_data": etl.data(counted_data)
                                                           })

