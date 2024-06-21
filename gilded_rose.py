# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        
    def update_quality(self):
        for item in self.items:
            if item.quality > 0 and item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name != "Sulfuras, Hand of Ragnaros":
                    #This if statement checks that the sell_in is passed the sell by date if yes
                    # the quality is halved by 2 else the quality decreses by 1
                    if item.sell_in <= 0:
                      
                        item.quality = item.quality - 2
                    else:
                        item.quality = item.quality - 1
                      
            elif item.quality < 50:
                # Aged Brie and Backstage passes will increase in quality as they get older. So what I did was 
                # to check that the name is either Aged Brie or Backstage passes and then add 1 to quality if it is backstage passes
                # and the backstage passes quality is equal to 49 (so that the highest quality it will add up to is 50) else if it is not equal to 49 which 
                # is if it is less than 49 then check if the sell by date is 10 or less if so add 2 to quality else if sell by date is 5 or less
                # then add 3 to quality else set quality to zero.
                 if item.name == "Backstage passes to a TAFKAL80ETC concert" and item.quality == 49 or item.name == "Aged Brie" and item.quality < 50:
                      item.quality = item.quality +  1
                 elif item.name == "Backstage passes to a TAFKAL80ETC concert" and item.quality < 49:
                    if item.sell_in <= 10:
                        item.quality = item.quality + 2
                    elif item.sell_in <= 5:
                        item.quality = item.quality + 3
                 if item.sell_in < 0 and item.name == "Backstage passes to a TAFKAL80ETC concert":
                        item.quality = 0
            
            item.sell_in = item.sell_in - 1
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
