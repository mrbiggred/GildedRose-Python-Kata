# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)

    def test_quality_degrades_twice_as_fast_after_sell_in(self):
        items = [Item("+5 Dexterity Vest", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("+5 Dexterity Vest", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(18, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
