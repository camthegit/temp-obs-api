import datetime
import uuid
from typing import List

from models.location import Location
from models.reports import Report

from models.site import Site
from models.observations import ObsReceived

__reports: List[Report] = []
__obslist: List[ObsReceived] = []
maxobslistlen = 50


async def get_reports() -> List[Report]:

    # Would be an async call here.
    return list(__reports)


async def add_report(description: str, location: Location) -> Report:
    now = datetime.datetime.now()
    report = Report(
        id=str(uuid.uuid4()),
        location=location,
        description=description,
        created_date=now)

    # Simulate saving to the DB.
    # Would be an async call here.
    __reports.append(report)

    __reports.sort(key=lambda r: r.created_date, reverse=True)

    return report


async def get_obs() -> List[ObsReceived]:

    # Would be an async call here.
    sel = __obslist[-5:]
    sel.sort(key=lambda r: r.created_date, reverse=True)
    return sel


async def add_obs(site: Site, temp: float, humidity: float, temp_exp: float) -> ObsReceived:
    now = datetime.datetime.now()
    obs = ObsReceived(
        id=str(uuid.uuid4()),
        location=site,
        temp=temp,
        humidity=humidity,
        temp_exp=temp_exp,
        created_date=now)

    # Simulate saving to the DB.
    # Would be an async call here.
    __obslist.append(obs)
    if len(__obslist) > maxobslistlen:
        __obslist.pop(0)

    # __obslist.sort(key=lambda r: r.created_date, reverse=True)

    return obs
