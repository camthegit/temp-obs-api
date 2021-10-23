import datetime
import uuid
from abc import ABC
from typing import Optional

# from pydantic import BaseModel
from odmantic import Field, Model, EmbeddedModel


# from models.site import Site


class Site(EmbeddedModel):
    city: Optional[str] = Field(None, example='Ourimbah')
    state: Optional[str] = 'NSW'
    country: str = 'AU'
    room: Optional[str] = Field(None, example='Study')
    description: Optional[str] = None


class ObsDetail(Model):
    # description: str
    temp: float
    humidity: float
    temp_exp: float
    volts: Optional[float] = Field(None, example=1.2)
    obsLocation: Optional[Site]
    sensor: Optional[str] = Field(None, example='64 bit address')
    saved: datetime.datetime

    class Config:
        collection = 'observations'


class ObsReceived(ObsDetail):
    # id: str
    created_date: Optional[datetime.datetime]
