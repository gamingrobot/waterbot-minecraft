import logging

from config import plugins, settings
from spockbot import Client

logger = logging.getLogger('spockbot')
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    client = Client(plugins=plugins, settings=settings)
    client.start()
