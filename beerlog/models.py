#from dataclasses import dataclass
#from unicodedata import name

#@dataclass
from typing import Optional
from sqlmodel import select
from sqlmodel import SQLModel, Field
#Para validação dos dados utilzamos a biblioteca pydantic
from pydantic import validator
from statistics import mean
class Beer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0

    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v

    def calculate_rate(cls, v, values):
        rate = mean

try:
    brewdog = Beer(name="Brewdog", style="NEIPA", flavor=6, image=8, cost=8)
except RuntimeError:
    print("Eita, deu zica!!")    