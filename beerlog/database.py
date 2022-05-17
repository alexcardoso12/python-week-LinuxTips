from sqlmodel import create_engine, Session
from beerlog.config import settings
from beerlog import models

# oracle://
# mysql://localhost:5555@user:pass/BDname

engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)