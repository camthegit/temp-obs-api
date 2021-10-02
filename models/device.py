from typing import Optional

from pydantic import BaseModel, Field
from models.core import PyObjectId
from bson import ObjectId
import datetime


class Device(BaseModel):
    time: datetime.datetime = Field(...)
    xbee_code: str = Field(...)
    volts: float = Field(...)

    class Config:
        id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "xbee_code": "1234 5678",
                "volts": "3.2",
                "time": "need a datetime here",
            }
        }