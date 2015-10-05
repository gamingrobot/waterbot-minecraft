
"""
Debug Plugin
"""

import logging

from spockbot.plugins.base import PluginBase

logger = logging.getLogger('spockbot')


class DebugPlugin(PluginBase):
    requires = ('ClientInfo', 'Entities', 'Movement', 'Interact', 'Inventory')
    events = {
        'inventory_synced': 'dostuff',

    }

    def __init__(self, ploader, settings):
        super(DebugPlugin, self).__init__(ploader, settings)

    def dostuff(self, name, data):
        self.testitem(386)

    def testitem(self, item):
        slot = self.inventory.find_slot(item, self.inventory.window.hotbar_slots)
        if slot is not None:
            self.inventory.select_active_slot(slot)
            self.interact.edit_book(["Hello", "World"])
            self.interact.sign_book("something", "something else")

