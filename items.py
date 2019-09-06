# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class Funds(scrapy.Item):
    stock_code = scrapy.Field()
    stock_market = scrapy.Field()
    stock_name = scrapy.Field()
    date = scrapy.Field()
    closePrice = scrapy.Field()
    quoteChange = scrapy.Field()
    inflow = scrapy.Field()
    mainForce = scrapy.Field()
    bigSingle = scrapy.Field()
    bigSingle1 = scrapy.Field()
    mediumSingle = scrapy.Field()
    mediumSingle1 = scrapy.Field()
    smallSingle = scrapy.Field()
    smallSingle1 = scrapy.Field()
    crawl_time = scrapy.Field()
