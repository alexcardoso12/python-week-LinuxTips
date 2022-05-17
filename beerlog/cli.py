
import typer
from typing import Optional
from beerlog.core import add_beer_to_database, get_beer_from_database

main = typer.Typer(help="Beer Management Application")


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    ### Adds a new beer to database ###
  if add_beer_to_database(name, style, flavor, image, cost):
      print("🍺 Beer added to Database")
  else:
      print("Há um erro nos dados passados. Tente novamente!")    

@main.command("list")
def list_beers(style: Optional[str] = None):
    ### Lists beers in database ###
    beers = get_beer_from_database()
    print(beers)