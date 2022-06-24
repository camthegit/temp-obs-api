
import motor.motor_asyncio  # may be installed with odomantic in requirements
import logging
import ssl
from data import mongo_setup
from odmantic import AIOEngine


logger = logging.getLogger(__name__)


def get_engine():
    client = motor.motor_asyncio.AsyncIOMotorClient(username='', password='', host='localhost', port=27017)
    # client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
    engine = AIOEngine(motor_client=client, database='weather')
    logger.debug(f'motor client created: {client.server_info()}')
    return engine


def global_engine(user=None, password=None, port=27017, server='localhost', use_ssl=True):
    if user or password:
        data = dict(
            username=user,
            password=password,
            host=server,
            port=port,
            authentication_source='admin',
            authentication_mechanism='SCRAM-SHA-1',
            ssl=use_ssl,
            ssl_cert_reqs=ssl.CERT_NONE)
        client = motor.motor_asyncio.AsyncIOMotorClient(**data)
        data['password'] = '*************'
        print(" --> Registering prod connection: {}".format(data))
    else:
        print(" --> Registering dev connection")
        client = motor.motor_asyncio.AsyncIOMotorClient(port=27017, host='localhost')

    engine = AIOEngine(motor_client=client, database='weather')
    logger.debug(f'motor client created: {client.server_info()}')
    return engine
