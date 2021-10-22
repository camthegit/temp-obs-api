import datetime
import uuid
from abc import ABC
from typing import Optional

# from pydantic import BaseModel
from odmantic import Field, Model, EmbeddedModel
# from models.site import Site


class Site(EmbeddedModel):
    city: Optional[str] = None
    state: Optional[str] = 'NSW'
    country: str = 'AU'
    room: Optional[str] = None
    description: Optional[str] = None


class ObsDetail(Model):
    # description: str
    temp: float
    humidity: float
    temp_exp: float
    obsLocation: Optional[Site]
    sensor: Optional[str] = None
    saved: datetime.datetime

    class Config:
        collection = 'observations'


class ObsReceived(ObsDetail):
    # id: str
    created_date: Optional[datetime.datetime]
