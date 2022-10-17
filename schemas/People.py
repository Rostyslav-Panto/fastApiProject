import datetime
from functools import lru_cache

import requests
from pydantic import BaseModel, Field, validator


@lru_cache(maxsize=None)
def get_homeworld_by_url(url):
    # Validation for JSON response and existing of planet with such id, url validation
    return requests.get(url).json().get("name")


class People(BaseModel):
    class Config:
        validate_assignment = True

    name: str
    birth_year: str
    eye_color: str
    gender: str
    hair_color: str
    height: str
    mass: str
    skin_color: str
    homeworld: str = Field(..., regex=r"https://swapi.dev/api/planets/+\d")
    date: datetime.date = Field(..., alias="edited")

    @validator('date', pre=True)
    def get_date_value(cls, value):
        d1 = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
        return d1.strftime("%Y-%m-%d")

    @validator('homeworld')
    def get_homeworld_name(cls, url):
        return get_homeworld_by_url(url)
