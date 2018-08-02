# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScanmapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    poi_name  = scrapy.Field
    poi_typecode = scrapy.Field
    poi_address = scrapy.Field
    poi_pcode = scrapy.Field
    poi_pname = scrapy.Field
    poi_citycode = scrapy.Field
    poi_adcode = scrapy.Field
    poi_adname = scrapy.Field
    poi_entr_location = scrapy.Field
    poi_tel = scrapy.Field
    poi_location = scrapy.Field
    pass
