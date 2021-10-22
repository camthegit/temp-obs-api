import datetime
import uuid
import logging
from typing import List

from models.location import Location
from models.reports import Report

# from models.site import Site
from models.observations import ObsDetail, ObsReceived, Site
from data.mongo_run import get_engine

__reports: List[Report] = []
__obslist: List[ObsReceived] = []
maxobslistlen = 50

logger = logging.getLogger(__name__)
logger.info(f'logger started at head of {__name__}')


async def get_reports() -> List[Report]:

    # Would be an async call here.
    return list(__reports)


async def add_report(description: str, location: Location) -> Report:
    """

    :param description:
    :type description:
    :param location:
    :type location:
    :return:
    :rtype:
    """
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


async def get_obs() -> List[ObsDetail]:
    db = get_engine()
    # Would be an async call here.
    sel = await db.find(ObsDetail, sort=ObsDetail.saved.desc(), limit=10)
    # sel = __obslist[-5:]
    # sel.sort(key=lambda r: r.saved, reverse=True)
    return sel


async def add_obs(site: Site, temp: float, humidity: float, temp_exp: float) -> ObsDetail:
    db = get_engine()  # refers to odmantic connection to 'weather'

    now = datetime.datetime.now()
    obs = ObsDetail(
        # id=str(uuid.uuid4()),
        obsLocation=site,
        temp=temp,
        humidity=humidity,
        temp_exp=temp_exp,
        saved=now)
    res = await db.save(obs)
    logger.debug('result %s' % repr(res))
    # Simulate saving to the DB.
    # Would be an async call here.
    # __obslist.append(obs)
    # if len(__obslist) > maxobslistlen:
    #     __obslist.pop(0)

    # __obslist.sort(key=lambda r: r.created_date, reverse=True)

    return res
