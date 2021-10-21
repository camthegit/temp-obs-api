import datetime
import uuid
from typing import Optional

# from pydantic import BaseModel
from odmantic import Field, Model
from models.site import Site


class ObsDetail(Model):
    # description: str
    temp: float
    humidity: float
    temp_exp: float
    obsLocation: Site
    sensor: Optional[str]


class ObsReceived(ObsDetail):
    id: str
    created_date: Optional[datetime.datetime]
