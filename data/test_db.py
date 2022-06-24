from models.observations import ObsDetail, ObsReceived
from data.mongo_run import global_engine
import logging
import datetime


logger = logging.getLogger(__name__)


async def test_mongo():
    # client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
    db = global_engine()  # refers to odmantic connection to 'weather'
    obs1 = ObsDetail(temp=37.5, humidity=55, temp_exp=40, saved=datetime.datetime.now())
    res = await db.save(obs1)
    logger.debug('result %s' % repr(res))
    # db = client.weather
    # coll = db.test_coll
    # loop = asyncio.get_event_loop()
    #
    # loop.run_until_complete(do_insert(coll))
    # client.closeimport datetime
    return repr(res)


if __name__ == "__main__":
    import asyncio

    asyncio.run(test_mongo())
