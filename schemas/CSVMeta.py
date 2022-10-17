import datetime

from pydantic import BaseModel


class CSVMeta(BaseModel):
    filename: str
    date: datetime.datetime

    class Config:
        orm_mode = True
