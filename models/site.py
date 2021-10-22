
from typing import Optional

from odmantic import EmbeddedModel
from pydantic import BaseModel
import datetime


class Site(EmbeddedModel):
    city: Optional[str] = None
    state: Optional[str] = 'NSW'
    country: str = 'AU'
    room: Optional[str] = None
    description: Optional[str] = None
    # inactive_from: Optional[datetime.datetime] = None
    # xbee_code: Optional[str] = None
