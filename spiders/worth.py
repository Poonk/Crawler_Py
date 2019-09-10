#-*-coding=utf-8-*-

import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

url = "http://basic.10jqka.com.cn/000001/worth.html#stockpage"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

# prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\test\\'}
# chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path="/mnt/c/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",chrome_options=chrome_options)
driver.get(url)
time.sleep(3)

trs = driver.find_elements_by_xpath("//*[@id='forecast']/div[2]/div[2]/div[1]/table//tr")

for tr in trs :
    a = tr.find_elements_by_xpath("/text")
    print(a)




