#-*-coding=utf-8-*-

import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def three_table():
    ul = driver.find_element_by_xpath("//*[@id='cwzbTable']/div[1]/ul")
    lis = ul.find_elements_by_tag_name("li")
    for li in lis :      
        li.click()
        time.sleep(1.5)
        driver.find_element_by_xpath("//*[@id='exportButton']").click()
        time.sleep(1.5)

    return 
 
url = 'http://basic.10jqka.com.cn/000001/finance.html#stockpage'
# request.urlretrieve("http://basic.10jqka.com.cn/000001/finance.html#stockpage","Income.txt")
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')

prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\test\\'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path="/mnt/c/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",chrome_options=chrome_options)
driver.get(url)
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


# 利润表
# a[contains(text(),"百度搜索")]
# //*[@id="cwzbDemo"]/div[2]/ul/li[3]/a
# //*[@id='cwzbDemo']/div[2]/ul/li[2]/a
# //*[@id="cwzbDemo"]/div[2]/ul/li[4]/a

# driver.quit()
