#预处理部分
import requests
import time
import re
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
driver_path = r'D:\ProjectPerson\firefoxdrive\geckodriver.exe'
driver = webdriver.Firefox(executable_path = driver_path)
#登录部分
target_url = 'https://www.weibo.com/login.php/'
#最大等待时间25s
wait = WebDriverWait(driver,25)
driver.get(target_url)
login = wait.until(EC.element_to_be_clickable((By.XPATH, '//li/a[@node-type="loginBtn"]')))
login.click()
#账号登录过程
try:
    username = input("input username:")
    password = input("input password:")
    user = wait.until(
            EC.presence_of_element_located((By.XPATH,'//div[@class = "item username input_wrap"]/input')))

    user.send_keys(username)
    pw = wait.until(
            EC.presence_of_element_located((By.XPATH,'//div[@class = "item password input_wrap"]/input')))

    pw.send_keys(password)
    pw.send_keys(Keys.ENTER)
except Exception as e:
    print(e)
#登录验证
if wait.until(EC.element_to_be_clickable((By.XPATH, '//strong[@node-type="follow"]'))):
    print('登录成功')
#获取相册AJAX源码
target_url = 'https://weibo.com/p/1005056697930990/photos?from=page_100505&mod=TAB#place'
driver.get(target_url)
with open('./AziPhotoSource.xml','w',encoding = 'utf-8') as sources:
    print(driver.page_source,file = sources)
#获取图片链接，(By.XPAHT)等待条件是Xpath里的所有节点出现
pictures = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="photo_cont"]/a/img')))
#将图片链接解析成连接
pics = []
for pic in pictures:
    try:
        cen_pic = pic.get_attribute('src')
        new_cen_pic = re.compile('\/\/.*?\/.*?\/(.*?)\?.*?').findall(cen_pic)
        pics.append('https://wx1.sinaimg.cn/mw1024/'+new_cen_pic[0])
    except Exception as e:
        print(e)
#Headers
Headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,'' like Gecko)Chr
ome/68.0.3440.106 Safari/537.36'}
#下载
for i in range(len(pics)):
     try:
             img = requests.get(pics[i],headers=Headers)
             if i % 20 ==0:
                     time.sleep(5)
             if img.status_code ==200:
                     with open('./pic'+str(i+1)+'.jpg','wb') as f:
                             f.write(img.content)
             else:
                     print('fail')
     except Exception as e:
         print('fail:',format(e))
