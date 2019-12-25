# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import csv

import scrapy

from collections import OrderedDict

from scrapy import Field, Item
import six

class OrderedItem(Item):
    def __init__(self, *args, **kwargs):
        self._values = OrderedDict()
        if args or kwargs:  # avoid creating dict for most common case
            for k, v in six.iteritems(dict(*args, **kwargs)):
                self[k] = v

    def __repr__(self):
        return csv.dumps(OrderedDict(self), ensure_ascii = False)


class BrandItem(scrapy.Item):
    car = scrapy.Field()
    price_range = scrapy.Field()
    url = scrapy.Field()


class SpecificItem(OrderedItem):
    car = scrapy.Field()
    group = scrapy.Field()
    price = scrapy.Field()
    reference_price = scrapy.Field()
    source_img = scrapy.Field()

class PoiItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    tel1 = scrapy.Field()
    tel2 = scrapy.Field()

class CarItem(scrapy.Item):
    car = scrapy.Field()
    price = scrapy.Field()