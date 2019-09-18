import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


url = 'http://stockpage.10jqka.com.cn/HK8238/'
# request.urlretrieve("http://basic.10jqka.com.cn/000001/finance.html#stockpage","Income.txt")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"')
# chrome_options.add_argument('--headless')

# prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\test\\'}
# chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path="/mnt/c/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",chrome_options=chrome_options)
driver.get(url)
time.sleep(5)

# print(driver.page_source)

# with open("test.txt","w") as f:
#         f.write(driver.page_source)


# marketValue = driver.find_element_by_xpath("/html/body/div[7]/div/ul[2]/li[1]/a").click()
marketValue = driver.find_elements_by_xpath("/html/body/div[7]/div/ul[2]")
print("1111")
for i in marketValue :
    print(i)
# print(marketValue)
