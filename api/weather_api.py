from typing import Optional, List

import fastapi
from fastapi import Depends

from models.location import Location
from models.reports import Report, ReportSubmittal
from models.observations import ObsReceived, ObsDetail
from models.validation_error import ValidationError
from services import openweather_service, report_service

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
async def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    try:
        return await openweather_service.get_report_async(loc.city, loc.state, loc.country, units)
    except ValidationError as ve:
        return fastapi.Response(content=ve.error_msg, status_code=ve.status_code)
    except Exception as x:
        return fastapi.Response(content=str(x), status_code=500)


@router.post('/api/reports', name='add_report', status_code=201, response_model=Report)
async def reports_post(report_submittal: ReportSubmittal) -> Report:
    d = report_submittal.description
    loc = report_submittal.location

    return await report_service.add_report(d, loc)


@router.get('/api/reports', name='all_reports', response_model=List[Report])
async def reports_get() -> List[Report]:
    # await report_service.add_report("A", Location(city="Portland"))
    # await report_service.add_report("B", Location(city="NYC"))
    return await report_service.get_reports()


@router.post('/api/obs', name='add_observation_set', status_code=201, response_model=ObsReceived)
async def obs_post(obs_detail: ObsDetail) -> ObsReceived:
    t = obs_detail.temp
    h = obs_detail.humidity
    te = obs_detail.temp_exp
    s = obs_detail.obsLocation

    return await report_service.add_obs(site=s, temp=t, humidity=h, temp_exp=te)


@router.get('/api/obs', name='all_observations', response_model=List[ObsReceived])
async def obs_get() -> List[ObsReceived]:
    # await report_service.add_obs(t, Location(city="Portland"))
    # await report_service.add_report("B", Location(city="NYC"))
    return await report_service.get_obs()
