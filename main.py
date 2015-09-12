from spock import Client
from config import plugins, settings

if __name__ == '__main__':
    client = Client(plugins=plugins, settings=settings)
    client.start()
