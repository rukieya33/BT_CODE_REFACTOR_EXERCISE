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

    def test_normal(self):
                items = [
                         Item("foo time", 25, 40),
                         ]
                gilded_rose = GildedRose(items)
                gilded_rose.update_quality()
                self.assertEqual(24, items[0].sell_in)
                self.assertEqual(38, items[0].quality)

    def test_quality_never_negative(self):
                items = [
                         Item("foo time", 5, 0),
                        ]
                gilded_rose = GildedRose(items)
                gilded_rose.update_quality()
                self.assertEqual(4, items[0].sell_in)
                self.assertEqual(0, items[0].quality)
                
    def test_max_quality(self):
                items = [
                         Item("foo time", 25, 49),
                         Item("Aged Brie", 10, 50),
                         Item("Backstage passes to a TAFKAL80ETC concert", 10, 50),
                        ]
                gilded_rose = GildedRose(items)
                gilded_rose.update_quality()
                self.assertEqual(24, items[0].sell_in)
                self.assertEqual(50, items[0].quality)
                self.assertEqual(9, items[1].sell_in)
                self.assertEqual(50, items[1].quality)
                self.assertEqual(9, items[2].sell_in)
                self.assertEqual(50, items[2].quality)
         
    def test_aged_brie(self):
                items = [
                         Item("Aged Brie", 10, 40),
                         ]
                gilded_rose = GildedRose(items)
                gilded_rose.update_quality()
                self.assertEqual(9, items[0].sell_in)
                self.assertEqual(41, items[0].quality)

    def test_backstage_passes(self):
                items = [
                         Item("Backstage passes to a TAFKAL80ETC concert", 10, 45),
                         Item("Backstage passes to a TAFKAL80ETC concert", 5, 15),
                         Item("Backstage passes to a TAFKAL80ETC concert", -1, 30),
                         ]
                gilded_rose = GildedRose(items)
                gilded_rose.update_quality()
                self.assertEqual(9, items[0].sell_in)
                self.assertEqual(47, items[0].quality)
                self.assertEqual(4, items[1].sell_in)
                self.assertEqual(18, items[1].quality)
                self.assertEqual(-2, items[1].sell_in)
                self.assertEqual(0, items[1].quality)

if __name__ == '__main__':
    unittest.main()
