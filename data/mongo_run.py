
import motor.motor_asyncio
import logging
from data import mongo_setup


logger = logging.getLogger(__name__)

def mongo_client():
    client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
    logger.debug(f'motor client created: {client.server_info()}')
    return client