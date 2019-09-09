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

    def parse(self, response):
        # title = response.xpath("//*[@id='in_squote']/div/h1/a[1]/strong/text()").extract()[0]
        # print(title)
        stock_code = '000001'
        stock_market = '1201'
        stock_name = '平安银行'

        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_experimental_option("profile.default_content_settings.popups", 0)
        # chrome_options.add_experimental_option("download.prompt_for_download", "false")
        # chrome_options.add_experimental_option("download.default_directory", "/mnt/d/test/")

        # chrome_options.add_experimental_option("prefs", {
        # "download.default_directory": "/mnt/d/test/",
        # "download.prompt_for_download": False,
        # "download.directory_upgrade": True,
        # "safebrowsing.enabled": True
        # })




        # prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': "/mnt/d/test"}

        # chrome_options.add_experimental_option('prefs', prefs)
        
        driver = webdriver.Chrome(executable_path="/mnt/c/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",chrome_options=chrome_options)

        driver.get(self.start_urls[0])
        

        time.sleep(5)

        # Income_statement =  driver.find_element(By.XPATH,"//*[@id='cwzbDemo']/div[2]/ul/li[3]/a").click()
        # Income_statement =  driver.find_element_by_xpath("//*[@id='cwzbDemo']/div[2]/ul/li[3]/a").click()
        # xpath_url = driver.find_element(By.XPATH,"//*[@id='exportButton']")
        # xpath_url = "//*[@id='exportButton']"
        # urls_pre = driver.find_elements_by_xpath("//*[@id='exportButton']/@href")
        # url = urls_pre[0].get_attribute("href")
        # url = drivers.find_element_by_xpath("//*[@id='exportButton']").get_attribute("href")

        # url = driver.find_element("//*[@id='exportButton']").click()

        try:
            driver.find_element_by_xpath("//*[@id='cwzbDemo']/div[2]/ul/li[3]/a").click()
        except :
            print("11111")

        
        try :
            driver.find_element_by_xpath("//*[@id='exportButton']").click()
        except :
            print("22222")
        

        # while 1:
        #     start = time.clock()
        #     try:
        #         driver.find_element_by_xpath("//*[@id='exportButton']").click()
        #         print ("已定位到元素2")
        #         sleep(3)
        #         end=time.clock()
        #         break
        #     except:
        #         print ("还未定位到元素2!")

        # print ('定位耗费时间：'+ str(end-start))


        # print(url)
        # driver.get(url)
        # request.urlretrieve(url, "Income.txt")
        # time.sleep(2)




        pass
