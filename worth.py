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

# 汇总--预测年报每股收益
# title_profit = driver.find_elements_by_xpath("//*[@id='forecast']/div[2]/div[2]/div[1]/table/caption")
# for title in title_profit:
#     print(title.text)
# print(title_profit)

# trs = driver.find_elements_by_xpath("//*[@id='forecast']/div[2]/div[2]/div[1]/table")
# for tr in trs :
#     print(tr.text)
#     print("\n")

# # 
# trs = driver.find_elements_by_xpath("//*[@id='forecast']/div[2]/div[2]/div[2]/table")
# for tr in trs :
#     print(tr.text)


trs = driver.find_elements_by_xpath("//*[@id='forecast']/div[2]/div[2]/div[1]/table/tbody/tr")
arr = []
arr1 = []
for tr in trs :
    print(tr.text)
    arr1 = (tr.text).split(" ")
    arr.append(arr1)
    # Year = tr.find_elements_by_xpath("./th").text
    # Forecast = tr.find_elements_by_xpath(".//td[1]").text
    # Minimum = tr.find_elements_by_xpath("./td[2]/text()").extract()[0]
    # Average = tr.find_elements_by_xpath("./td[3]/text()").extract()[0]
    # Maximum = tr.find_elements_by_xpath("./td[4]/text()").extract()[0]
    # Industry = tr.find_elements_by_xpath("./td[5]/text()").extract()[0]
    # print(Year,Forecast,Minimum,Average,Maximum,Industry)
    # print(Forecast)
    # print(tr)
    # print("1111")

print("111")



for i in range(len(arr)) :
    for j in range(len(arr[i])) :
        print(i,"\t",j,"\t",arr[i][j])
        # Year = [i][0]
        # Forecast = [i][1]
        # Minimum = [i][2]
        # Average = [i][3]
        # Maximum = [i][4]
        # Industry = [i][5]
        # print(Year,Forecast,Minimum,Average,Maximum,Industry)
    #     lts.append(Year)
    #     lts.append(Forecast)
    #     lts.append(Minimum)
    #     lts.append(Average)
    #     lts.append(Maximum)
    #     lts.append(Industry)
    # lt.append(lts)

# print("\n")

# lt = []
# lts = []

# for i in range(len(lt)):
#     for j in range(len(lt[i])):
#         print(i,"\t",j,"\t",lt[i][j])



