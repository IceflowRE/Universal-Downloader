import unittest
from datetime import datetime

from packaging.version import InvalidVersion

from unidown.plugins.data.link_item import LinkItem


class LinkItemTest(unittest.TestCase):
    def setUp(self):
        self.item = LinkItem('blub', datetime(1996, 12, 4))

    def test_equality(self):
        with self.subTest(desc="different type"):
            self.assertFalse(self.item == "blub")
            self.assertTrue(self.item != "blub")
        with self.subTest(desc="equal"):
            item = LinkItem('blub', datetime(1996, 12, 4))
            self.assertTrue(self.item == item)
            self.assertFalse(self.item != item)
        with self.subTest(desc="unequal"):
            item = LinkItem('whatever', datetime(1996, 12, 4))
            self.assertFalse(self.item == item)
            self.assertTrue(self.item != item)
            item = LinkItem('blub', datetime(2000, 12, 4))
            self.assertFalse(self.item == item)
            self.assertTrue(self.item != item)

    def test_str(self):
        self.assertEqual('(blub, 1996-12-04 00:00:00)', str(self.item))
