from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from getlink import *
from download import DownloadPhoto
import re
import time

driver_path = r'd:/ProjectPerson/firefoxdrive/geckodriver.exe'
driver = webdriver.Firefox(executable_path = driver_path)
target = 'https://cn.bing.com'
driver.get(target)

#webSources = driver.page_source
#soupStr = BeautifulSoup(webSources)
#formatStr = soupStr.prettify()
#find_links = soupStr.find_all('link')
#print(find_links)
#wait = WebDriverWait(driver,25)

index = 1
previousLink = ''
while index > 0:
    if index >1:
        preview = driver.find_element_by_id('sh_lt')
        ActionChains(driver).double_click(preview).perform()
        time.sleep(2)
        webSources = driver.page_source
        linkGet = DivLink()
    else:
        webSources = driver.page_source
        linkGet = HrefLink()
    photoDownload = DownloadPhoto()
    downloadlink = linkGet.analysis(webSources)
    if previousLink == downloadlink:
        print('Scrapy Done')
        break
    previousLink = downloadlink
    print(str(index)+':'+downloadlink)
    if downloadlink != 'fail':
        photoDownload.get(downloadlink)
    else:
        print("can't download,links="+downloadlink)
    index += 1
driver.close()
    
'''
soupStr = BeautifulSoup(webSources)
formatStr = soupStr.prettify()
find_links = soupStr.find(id="bgDiv")
print(find_links)
'''

'''
def getlink(file):
    readfile = open(file,'r',encoding = 'utf-8')
    links = BeautifulSoup(readfile.read())
    readfile.close()
    links.find_all('link')
    print('\n\n')
    lin = links.find_all('link')
    for i in lin:
    print(i)
'''
