# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# class Funds(scrapy.Item):
#     stock_code = scrapy.Field()
#     stock_market = scrapy.Field()
#     stock_name = scrapy.Field()
#     data = scrapy.Field()

class Holder(scrapy.Item):
    stock_code = scrapy.Field()
    stock_market = scrapy.Field()
    stock_name = scrapy.Field()
    data = scrapy.Field()
    crawl_time = scrapy.Field()

class Index(scrapy.Item):
    industry = scrapy.Field()
    marketValue = scrapy.Field()
    circulationValue = scrapy.Field()
    PER = scrapy.Field()
    PBR = scrapy.Field()
    capitalAmount = scrapy.Field()
    gain = scrapy.Field()

    
