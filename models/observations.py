import datetime
import uuid
from typing import Optional

from pydantic import BaseModel

from models.site import Site


class ObsDetail(BaseModel):
    # description: str
    temp: float
    humidity: float
    temp_exp: float
    obsLocation: Site


class ObsReceived(ObsDetail):
    id: str
    created_date: Optional[datetime.datetime]
