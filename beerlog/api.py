from urllib import response
from fastapi import FastAPI   #ASGI
from beerlog.core import get_beer_from_database
from beerlog.serializers import BeerIn, BeerOut
from typing import List
from beerlog.database import get_session
from beerlog.models import Beer
#from beerlog.models import Beer

api = FastAPI(title='Beerlog')

#@api.get("/beers/", response_model=List[Beer])
@api.get("/beers/", response_model=List[BeerOut])
def list_beers():
    beers = get_beer_from_database()
    return beers

#Adicionando uma nova Rota com a inserção diretamente no api.py
@api.post("/beers/", response_model=BeerOut)
def add_beer(beer_in: BeerIn):
    beer =Beer(**beer_in.dict())
    with get_session() as session:
        session.add(beer)
        session.commit()
        session.refresh(beer) #Objeto sem ID
    return beer