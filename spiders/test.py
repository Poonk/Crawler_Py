import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from urllib import request

url = 'http://basic.10jqka.com.cn/000001/finance.html#stockpage'
# request.urlretrieve("http://basic.10jqka.com.cn/000001/finance.html#stockpage","Income.txt")
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path="/mnt/c/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",chrome_options=chrome_options)
driver.get(url)
time.sleep(5)
try:
    driver.find_element_by_xpath("//*[@id='cwzbDemo']/div[2]/ul/li[3]/a").click()
except :
    print("11111")

try :
    driver.find_element_by_xpath("//*[@id='exportButton']").click()
except :
    print("22222")


