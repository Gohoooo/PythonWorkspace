import requests
import pandas as pd
import openpyxl as op

headers = {"User=Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
url = "https://comic.naver.com/api/webtoon/titlelist/weekday?order=user"
res = requests.get(url, headers=headers)
res.raise_for_status()

listRes = requests.get(url=url, headers=headers).json()

webtoonS = ''
webtoonT = ''
row = 0

df1 = pd.DataFrame({'웹툰제목':[], '웹툰링크':[]})

for i in listRes['titleListMap'] :
    #  print(i)
     for j in listRes['titleListMap'][i] :
        #   print(j['titleName'] + ' : https://comic.naver.com/webtoon/list?titleId=' + str(j['titleId'])) 

        webtoonS = j['titleName']
        webtoonT = 'https://comic.naver.com/webtoon/list?titleId=' + str(j['titleId'])

        df1.loc[row] = [webtoonS, webtoonT]
        row += 1

# # webtoonS = webtoonS[1:len(webtoonS)]
# # webtoonT = webtoonT[1:len(webtoonT)]    

# print(df1)

df1.to_excel(excel_writer='C:/Users/go_he/OneDrive/바탕 화면/PythonWork/practice.xlsx')