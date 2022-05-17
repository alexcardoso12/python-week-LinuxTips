# from dataclasses import dataclass
# from unicodedata import name

# @dataclass
# Para validação dos dados utilzamos a biblioteca pydantic
from typing import Optional
from tomlkit import date
from sqlmodel import select
from sqlmodel import SQLModel, Field
from pydantic import validator
from statistics import mean
from datetime import datetime


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)

    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v

    @validator("rate", always=True)
    def calculate_rate(cls, v, values):
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return int(rate)


try:
    brewdog = Beer(name="Brewdog", style="NEIPA", flavor=6, image=8, cost=8)
except RuntimeError:
    print("Eita, deu zica!!")
