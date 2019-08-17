from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from getlink import Link
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

wait = WebDriverWait(driver,25)
preview = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="sh_lt"]')))
preview.click()
preview.click()
time.sleep(3)
webSources = driver.page_source

linkGet = Link()
photoDownload = DownloadPhoto()
downloadlink = linkGet.analysis(webSources)
if downloadlink != 'fail':
    photoDownload.get(downloadlink)
else:
    print("can't download,links="+downloadlink)


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
