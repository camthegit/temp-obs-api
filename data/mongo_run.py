
import motor.motor_asyncio  # may be installed with odomantic in requirements
import logging
from data import mongo_setup
from odmantic import AIOEngine


logger = logging.getLogger(__name__)


def get_engine():
    client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
    engine = AIOEngine(motor_client=client, database='weather')
    logger.debug(f'motor client created: {client.server_info()}')
    return engine
