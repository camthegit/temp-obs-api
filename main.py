import asyncio
import json
from pathlib import Path

import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles
# import motor.motor_asyncio
import logging
import logging.config
from log_settings import LOGGING_CONFIG
from pythonjsonlogger import jsonlogger

from api import weather_api
# from data import mongo_setup  # need to configure authentication for server
from data.mongo_run import get_engine
from data import test_db
from services import openweather_service
from views import home
from configs import cnf
from models import observations
import asyncio

api = fastapi.FastAPI()
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)
logger.info('logger started at head of main')

def configure():

    logger.debug('attempt to log again', extra={'tester': 'ctp'})
    configure_routing()
    configure_api_keys()
    configure_fake_data()
    # mongo_setup.global_init()  # no authentication set
    asyncio.run(test_db.test_mongo())


def configure_api_keys():
    openweather_service.api_key = cnf.OWS_API_KEY
    # file = Path('settings.json').absolute()
    # if not file.exists():
    #     print(f"WARNING: {file} file not found, you cannot continue, please see settings_template.json")
    #     raise Exception("settings.json file not found, you cannot continue, please see settings_template.json")
    #
    # with open('settings.json') as fin:
    #     settings = json.load(fin)
    #     openweather_service.api_key = settings.get('api_key')


# async def test_mongo():
#     # client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
#     db = get_engine()  # refers to odmantic connection to 'weather'
#     ob1 = ObsDetail(temp=37.5, humidity=65, temp_exp=40)
#     res = await db.save(obs1)
#     logger.debug('result %s' % repr(res.inserted_id))
#     # db = client.weather
#     # coll = db.test_coll
#     # loop = asyncio.get_event_loop()
#     #
#     # loop.run_until_complete(do_insert(coll))
#     # client.close


async def do_insert(coll):
    document = {'temp_test': '99'}
    result = await coll.insert_one(document)
    print('result %s' % repr(result.inserted_id))


def configure_routing():
    api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)


def configure_fake_data():
    # This was added to make it easier to test the weather event reporting
    # We have /api/reports but until you submit new data each run, it's missing
    # So this will give us something to start from.
    pass  # Doesn't work on Ubuntu under gunicorn
    # try:
    #     loc = Location(city="Portland", state="OR", country="US")
    #     asyncio.run(report_service.add_report("Misty sunrise today, beautiful!", loc))
    #     asyncio.run(report_service.add_report("Clouds over downtown.", loc))
    # except:
    #     print("NOTICE: Add default data not supported on this system (usually under uvicorn on linux)")


if __name__ == '__main__':
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    configure()
