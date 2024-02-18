from bs4 import BeautifulSoup
import requests
import warnings
import json
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from tqdm import tqdm

warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

driver = webdriver.Chrome()
driver.implicitly_wait(3)

# host = 'brd.superproxy.io:22225'
# user_name = 'brd-customer-hl_111b508b-zone-unblocker'
# password = 'z8l9602yshyy'
# proxy_url = f'https://{user_name}:{password}@{host}'
# proxies = {'http': proxy_url, 'https': proxy_url}

url = 'https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx'
driver.get(url)
# driver.maximize_window()
# print(driver.find_element(By.TAG_NAME, 'select'))
# print(driver.find_elements(By.TAG_NAME, 'select'))
# print(driver.find_element(By.CLASS_NAME, 'select02').text)

year_list = [x.strip() for x in driver.find_element(By.CLASS_NAME, 'select02').text.split('\n')\
             if len(x) > 1 ]


# driver.find_element(By.CLASS_NAME, 'select02').click()
# xpath_format = '//option[@value="2019"]'
# driver.find_element(By.XPATH, xpath_format.format(value = '2019')).click()

# print(year_list)


for year in year_list :

    
    if year == '전체' : continue
    if int(year) < 2019 : continue
    
    print(year)

    driver.find_element(By.CLASS_NAME, 'select02').click()
    xpath_format = '//option[@value=' + year + ']'
    driver.find_element(By.XPATH, xpath_format.format(value = year)).click()
    print('년도선택####')
    time.sleep(3)

    for page_num in range(1, 35) :
        
        btnNum = 'cphContents_cphContents_cphContents_ucPager_btnNo' + str(page_num)
    
        pageCnt = driver.find_elements(By.ID, btnNum)

        if not pageCnt : break

        for j in pageCnt :

            driver.find_element(By.ID, btnNum).click()      
            time.sleep(3)

            print(driver.find_element(By.TAG_NAME, 'Table').text)
            

            


    # asghsdg = 'cphContents_cphContents_cphContents_ucPager_btnNo' + '1'
    # stgsdg = driver.find_element(By.ID, asghsdg)
    # driver.find_element(By.ID, 'cphContents_cphContents_cphContents_ucPager_btnNo3').click()
    # print(stgsdg)
    # time.sleep(3)

    
    # print(driver.find_element(By.ID, 'cphContents_cphContents_cphContents_ucPager_btnNo2').text)
    # driver.find_element(By.ID, 'cphContents_cphContents_cphContents_ucPager_btnNo1').click()
    # time.sleep(3)                                
    # driver.find_element(By.ID, 'cphContents_cphContents_cphContents_ucPager_btnNo2').click()
    # time.sleep(3)
  


    # print(driver.find_element(By.TAG_NAME, 'Table').text)

    

    time.sleep(3)

time.sleep(3)


# items = driver.find_elements(By.CLASS_NAME, 'select02')

# for item in items : 

#     print(item.text)

# res = requests.get(url, proxies=proxies, verify=False)
# html = res.text
# soup = BeautifulSoup(html, "html.parser")


