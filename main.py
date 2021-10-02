import asyncio
import json
from pathlib import Path

import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles
import motor.motor_asyncio
import logging
# from log_settings import LOGGING_CONFIG

from api import weather_api
from data import mongo_setup  # need to configure authentication for server
from services import openweather_service
from views import home
from configs import cnf

api = fastapi.FastAPI()


def start_logging():
    pass


def configure():
    configure_routing()
    configure_api_keys()
    configure_fake_data()
    # mongo_setup.global_init()  # no authentication set
    start_logging()
    start_mongo()


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


def start_mongo():
    client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
    db = client.weather
    coll = db.test_coll
    loop = asyncio.get_event_loop()

    loop.run_until_complete(do_insert(coll))


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
