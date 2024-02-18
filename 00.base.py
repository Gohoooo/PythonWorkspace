from bs4 import BeautifulSoup
import requests
import warnings
import json
import pandas as pd
import openpyxl as op

warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

host = 'brd.superproxy.io:22225'
user_name = 'brd-customer-hl_111b508b-zone-unblocker'
password = 'z8l9602yshyy'
proxy_url = f'https://{user_name}:{password}@{host}'

proxies = {'http': proxy_url, 'https': proxy_url}

url = ''
res = requests.get(url, proxies=proxies, verify=False)
html = res.text
soup = BeautifulSoup(html, "html.parser")

print(soup)