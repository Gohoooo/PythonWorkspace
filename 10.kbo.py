from bs4 import BeautifulSoup
import requests
import warnings
import json
import pandas as pd
import openpyxl as op
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

row = 0
df1 = pd.DataFrame({'순위':[], '선수명':[], '팀명':[], 'AVG':[], 'G':[], 'PA':[], 'AB':[], 'R':[]
                  , 'H':[], '2B':[], '3B':[], 'HR':[], 'TB':[], 'RBI':[], 'SAC':[], 'SF':[]})

for year in year_list :

    
    if year == '전체' : continue
    if int(year) < 2020 : continue
    
    print(year)

    driver.find_element(By.CLASS_NAME, 'select02').click()
    time.sleep(2)
    xpath_format = '//option[@value=' + year + ']'
    driver.find_element(By.XPATH, xpath_format.format(value = year)).click()
    time.sleep(2)

    for page_num in range(1, 35) :
        
        btnNum = 'cphContents_cphContents_cphContents_ucPager_btnNo' + str(page_num)
    
        pageCnt = driver.find_elements(By.ID, btnNum)

        if not pageCnt : break

        for j in pageCnt :

            driver.find_element(By.ID, btnNum).click()      
            time.sleep(2)

            for k in driver.find_elements(By.TAG_NAME, 'tr') : 

                listRst = []

                for n in k.find_elements(By.TAG_NAME, 'td') :

                    listRst.append(n.text)
            # player_list = [x.strip() for x in driver.find_element(By.TAG_NAME, 'Table').text.split('\n')]

            # print(player_list)
                
                if not listRst : continue
                
                df1.loc[row] = listRst
                row += 1

df1.to_excel(excel_writer='C:/Users/go_he/OneDrive/바탕 화면/PythonWork/kbo_01.xlsx')



