"""
Echos cha
"""

import logging

from spock.plugins.base import PluginBase
from spock.utils import pl_announce

logger = logging.getLogger('spock')


@pl_announce('ChatEchoPlugin')
class ChatEchoPlugin(PluginBase):
    #requires = ('Chat')
    events = {
        'chat': 'handle_chat',
    }

    def handle_chat(self, name, data):
        logger.info(data)
