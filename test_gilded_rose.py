# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo_sell_in(self):
        items = [Item("foo", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(14, items[0].sell_in)

    def test_foo_quality(self):
            items = [Item("foo", 15, 20)]
            gilded_rose = GildedRose(items)
            gilded_rose.update_quality()
            self.assertEqual(19, items[0].quality)


        
if __name__ == '__main__':
    unittest.main()
