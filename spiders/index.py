# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import Index
from selenium import webdriver

class IndexSpider(scrapy.Spider):
    name = 'index'
    allowed_domains = ['http://stockpage.10jqka.com.cn/HK8238/']
    start_urls = ['http://stockpage.10jqka.com.cn/HK8238//']

     
    def parse(self, response):
        industry = response.xpath("//ul[@class='detail_list cb fl']/li/a/text()").extract()[0]
        marketValue = response.xpath("//ul[@class='detail_list cb fl']/li[2]/strong/text()").extract()[0]
        circulationValue = response.xpath("//ul[@class='detail_list cb fl']/li[3]/strong/text()").extract()[0]
        PER = response.xpath("//ul[@class='detail_list cb fl']/li[4]/strong/text()").extract()[0]
        PBR = response.xpath("//ul[@class='detail_list cb fl']/li[5]/strong/text()").extract()[0]
        capitalAmount = response.xpath("//div[@class='sub_cont_3']/dl/dd[1]/text()").extract()[0]
        gain = response.xpath("//div[@class='sub_cont_3']/dl/dd[3]/text()").extract()[0]

        print(industry,marketValue,circulationValue,PER,PBR,capitalAmount,gain)
        # print(industry,marketValue)

        pass
