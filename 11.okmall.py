from bs4 import BeautifulSoup
import requests
import warnings
import json
import pandas as pd
import openpyxl as op
from urllib import parse
from tkinter import *

warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

host = 'brd.superproxy.io:22225'
user_name = 'brd-customer-hl_111b508b-zone-unblocker'
password = 'z8l9602yshyy'
proxy_url = f'https://{user_name}:{password}@{host}'

proxies = {'http': proxy_url, 'https': proxy_url}

url = 'https://www.okmall.com/html_data/gnb/V1/top_all_brand_V5.html'
res = requests.get(url, proxies=proxies, verify=False)
res.encoding='UTF-8'
html = res.text
soup = BeautifulSoup(html, "html.parser")

baseList1 = soup.find(class_='allBrand_list')
baseList2 = baseList1.find_all('li')

root = Tk()
root.geometry('1000x800+500+130')
root.title("Goho proctice")
frame = Frame(root).pack()
scrollbar = Scrollbar(root)
scrollbar.pack(side='right', fill='y')
listbox = Listbox(frame, selectmode='extended', height=10, yscrollcommand=scrollbar.set)

for i in baseList2 :
    
    brandText = i.find(class_='t_nm').text
    href = i.find('a')
    hrefText = href.attrs['href']
    
    print(str(brandText) + ' : ' + 'https://www.okmall.com/' + str(hrefText))
    # print(i.find(class_='t_nm'))

    # btn = Button(root, text=brandText)
    # btn.pack()
    listbox.insert(END, brandText)
    listbox.pack()


scrollbar.config(command=listbox.yview)

root.mainloop()