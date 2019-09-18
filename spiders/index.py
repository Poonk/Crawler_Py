# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import Index

class IndexSpider(scrapy.Spider):
    name = 'index'
    allowed_domains = ['http://stockpage.10jqka.com.cn/HK8238/']
    start_urls = ['http://stockpage.10jqka.com.cn/HK8238//']

    def parse(self, response):
        industry = response.xpath("/html/body/div[7]/div/ul[2]/li[1]/a/text()").extract()[0]
        marketValue = response.xpath("/html/body/div[7]/div/ul[2]/li[2]/text()")
        circulationValue = response.xpath("/html/body/div[7]/div/ul[2]/li[3]/strong/text()").extract()[0]
        PER = response.xpath("/html/body/div[7]/div/ul[2]/li[4]/strong/text()").extract()[0]
        PBR = response.xpath("/html/body/div[7]/div/ul[2]/li[5]/strong").extract()[0]
        capitalAmount = response.xpath("/html/body/div[9]/div[6]/div[3]/dl/dd[1]/text()").extract()[0]
        gain = response.xpath("/html/body/div[9]/div[6]/div[3]/dl/dd[3]/text()").extract()[0]

        print(industry,marketValue,circulationValue,PER,PBR,capitalAmount,gain)

        pass
