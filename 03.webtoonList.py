import requests

headers = {"User=Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
url = "https://comic.naver.com/api/webtoon/titlelist/weekday?order=user"
res = requests.get(url, headers=headers)
res.raise_for_status()

listRes = requests.get(url=url, headers=headers).json()

# print(listRes)
# print(listRes['titleListMap'])
# print(listRes['totalRankingTitleList'][1]['titleName'])
for i in listRes['titleListMap'] :
     
     print(i)
     for j in listRes['titleListMap'][i] :
          print(j['titleName']) 
          

