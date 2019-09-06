# -*- coding: utf-8 -*-
import scrapy
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class FinanceSpider(scrapy.Spider):
    name = 'finance'
    allowed_domains = ['http://stockpage.10jqka.com.cn']
    start_urls = ['http://stockpage.10jqka.com.cn/000001/finance/']

    def parse(self, response):
        title = response.xpath("//*[@id='in_squote']/div/h1/a[1]/strong/text()").extract()[0]
        print(title)

        driver = webdriver.Chrome(executable_path="/mnt/c/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
        driver.get(self.start_urls[0])

        time.sleep(2)

        # url = driver.find_element(By.XPATH,"//*[@id='exportButton']/@href")
        # url = driver.find_element_by_partial_link_text('导出数据')
        text = driver.page_source
        print(text)



        pass
