import requests

headers = {"User=Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
url = "https://comic.naver.com/api/realtime/ranking/list?rankTabType=DEFAULT"
res = requests.get(url, headers=headers)
res.raise_for_status()

listRes = requests.get(url=url, headers=headers).json()

print(listRes['totalRankingTitleList'])


# print(listRes['totalRankingTitleList'][0]['titleName'])
# print(listRes['totalRankingTitleList'][1]['titleName'])

# for a in listRes['totalRankingTitleList'] :
#      print(a['titleName'] + ' : https://comic.naver.com/webtoon/list?titleId=' + str(a['titleId']))



# https://comic.naver.com/webtoon/list?titleId=

# for listRes1 in listRes :
#      print("1")
