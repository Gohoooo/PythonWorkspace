import requests

headers = {"User=Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
url = "https://comic.naver.com/api/realtime/ranking/list?rankTabType=DEFAULT"
res = requests.get(url, headers=headers)
res.raise_for_status()

listRes = requests.get(url=url, headers=headers).json()

print(listRes)

# listRes = requests.get(url=url, headers=headers).json()

# print(listRes['items'])

# response = requests.get(url='던질유알엘', headers='헤더').json()

# soup = BeautifulSoup(res.text, "lxml")

# print(soup.text)

# print(soup.find("titleId"))
# print(soup.find_all("li", attrs={"class":"Poster__link--sopnC"}))

# print(soup.title)
# print(soup.title.get_text()) 
# print(soup.a) 
# print(soup.a["href"]) 

# soup.find_all("li")

# print(soup.find(")

