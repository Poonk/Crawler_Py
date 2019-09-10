# -*- coding: utf-8 -*-
import scrapy
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from urllib import request


class FinanceSpider(scrapy.Spider):
    name = 'finance'
    allowed_domains = ['http://stockpage.10jqka.com.cn']
    start_urls = ['http://basic.10jqka.com.cn/000001/finance.html#stockpage']

    def three_table(self):
        ul = driver.find_element_by_xpath("//*[@id='cwzbTable']/div[1]/ul")
        lis = ul.find_elements_by_tag_name("li")
        for li in lis :      
            li.click()
            time.sleep(1.5)
            driver.find_element_by_xpath("//*[@id='exportButton']").click()
            time.sleep(1.5)


    def parse(self, response):
        # title = response.xpath("//*[@id='in_squote']/div/h1/a[1]/strong/text()").extract()[0]
        # print(title)
        stock_code = '000001'
        stock_market = '1201'
        stock_name = '平安银行'

        self.chrome_options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\test\\'}
        self.chrome_options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(executable_path="/mnt/c/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",chrome_options=chrome_options)
        driver.get(self.start_urls)
        time.sleep(3)


        # 资产负债表
        driver.find_element_by_xpath("//*[@id='cwzbDemo']/div[2]/ul/li/a[contains(text(),'资产负债表')]").click()
        three_table()

        # 利润表
        driver.find_element_by_xpath("//*[@id='cwzbDemo']/div[2]/ul/li/a[contains(text(),'利润表')]").click()
        three_table()

        # 现金流量表
        driver.find_element_by_xpath("//*[@id='cwzbDemo']/div[2]/ul/li/a[contains(text(),'现金流量表')]").click()
        three_table()

        pass
