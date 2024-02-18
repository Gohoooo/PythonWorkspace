from bs4 import BeautifulSoup
import requests
import warnings

warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

host = 'brd.superproxy.io:22225'
user_name = 'brd-customer-hl_111b508b-zone-unblocker'
password = 'z8l9602yshyy'
proxy_url = f'https://{user_name}:{password}@{host}'

proxies = {'http': proxy_url, 'https': proxy_url}

url = 'https://gall.dcinside.com/board/lists/?id=dcbest'
res = requests.get(url, proxies=proxies, verify=False)
html = res.text
soup = BeautifulSoup(html, "html.parser")

#items = soup.select("[class=ub-content us-post]")
link = soup.find_all("tr", {"class" : "ub-content us-post"})

#print(items.text)

for item in link : 

    #name = item.select_one(".gall_num").text
    name = item.find("td", {"class" : "gall_num"})
    print(name.text)
