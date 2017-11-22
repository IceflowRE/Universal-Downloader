import unittest
from datetime import datetime

from packaging.version import Version

from unidown.plugins.data.link_item import LinkItem
from unidown.plugins.data.plugin_info import PluginInfo
from unidown.plugins.data.save_state import SaveState


class SaveStateTest(unittest.TestCase):
    def setUp(self):
        self.save = SaveState(Version('1'), PluginInfo('Blub', '1.0.0', 'example.com'), datetime(1996, 12, 4),
                              {'item': LinkItem('blub', datetime(1996, 12, 4))})

    def test_equality(self):
        with self.subTest(desc="different type"):
            self.assertFalse(self.save == "blub")
            self.assertTrue(self.save != "blub")
        with self.subTest(desc="equal"):
            save = SaveState(Version('1'), PluginInfo('Blub', '1.0.0', 'example.com'), datetime(1996, 12, 4),
                             {'item': LinkItem('blub', datetime(1996, 12, 4))})
            self.assertTrue(self.save == save)
            self.assertFalse(self.save != save)
        with self.subTest(desc="unequal"):
            save = SaveState(Version('2'), PluginInfo('Blub', '1.0.0', 'example.com'), datetime(1996, 12, 4),
                             {'item': LinkItem('blub', datetime(1996, 12, 4))})
            self.assertFalse(self.save == save)
            self.assertTrue(self.save != save)
            save = SaveState(Version('1'), PluginInfo('whatever', '1.0.0', 'example.com'), datetime(1996, 12, 4),
                             {'item': LinkItem('blub', datetime(1996, 12, 4))})
            self.assertFalse(self.save == save)
            self.assertTrue(self.save != save)
            save = SaveState(Version('1'), PluginInfo('Blub', '1.0.0', 'example.com'), datetime(2000, 12, 4),
                             {'item': LinkItem('blub', datetime(1996, 12, 4))})
            self.assertFalse(self.save == save)
            self.assertTrue(self.save != save)
            save = SaveState(Version('1'), PluginInfo('Blub', '1.0.0', 'example.com'), datetime(1996, 12, 4),
                             {'item2': LinkItem('blub', datetime(1996, 12, 4))})
            self.assertFalse(self.save == save)
            self.assertTrue(self.save != save)
            save = SaveState(Version('1'), PluginInfo('Blub', '1.0.0', 'example.com'), datetime(1996, 12, 4),
                             {'item': LinkItem('blub', datetime(2000, 12, 4))})
            self.assertFalse(self.save == save)
            self.assertTrue(self.save != save)
