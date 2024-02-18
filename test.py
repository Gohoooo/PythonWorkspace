from bs4 import BeautifulSoup
import requests
import warnings
import json

warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

host = 'brd.superproxy.io:22225'
user_name = 'brd-customer-hl_111b508b-zone-unblocker'
password = 'z8l9602yshyy'
proxy_url = f'https://{user_name}:{password}@{host}'

proxies = {'http': proxy_url, 'https': proxy_url}

url = 'https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx'
res = requests.get(url, proxies=proxies, verify=False)
html = res.text
soup = BeautifulSoup(html, "html.parser")


# listRes = soup.select("[class=record_result]")
listRes1 = soup.find(class_ = 'sub-content')
listRes2 = listRes1.find(class_ = 'compare schItem')
listRes3 = listRes2.find_all('option')

print(listRes3)




