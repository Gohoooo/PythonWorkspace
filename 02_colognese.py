 # https://www.colognese.com/woman/?page=46
    # https://www.colognese.com/woman/?categories=accessories&page=
    # https://www.colognese.com/woman/?categories=bags&page=
    # https://www.colognese.com/woman/?categories=clothing&page=
    # https://www.colognese.com/woman/?categories=jewellery&page=
    # https://www.colognese.com/woman/?categories=shoes&page=
    
# https://www.colognese.com/man/?page=30
    # https://www.colognese.com/man/?categories=accessories&page=
    # https://www.colognese.com/man/?categories=bags&page=
    # https://www.colognese.com/man/?categories=clothing&page=
    # https://www.colognese.com/man/?categories=shoes&page=

# https://www.colognese.com/kids/?page=7
    # https://www.colognese.com/kids/?categories=accessories&page=
    # https://www.colognese.com/kids/?categories=clothing&page=
    # https://www.colognese.com/kids/?categories=shoes&page=

# https://www.colognese.com/outlet/?page=18
    # https://www.colognese.com/outlet/?categories=man&page=
    # https://www.colognese.com/outlet/?categories=kids&page=
    # https://www.colognese.com/outlet/?categories=woman&page=

# https://www.colognese.com/lifestyle/

from bs4 import BeautifulSoup
import requests
import warnings
import json
import pandas as pd
import openpyxl as op
import math
from currency_converter import CurrencyConverter

c = CurrencyConverter()


warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

# 제품명/제품id (sku number)/브랜드네임 / 카테고리코드 / 
# 이미지 사진 모두 / 옵션(사이즈 등) / 재고 수량 / 세일가 / 원가격

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
host = 'brd.superproxy.io:22225'
user_name = 'brd-customer-hl_111b508b-zone-unblocker'
password = 'z8l9602yshyy'
proxy_url = f'https://{user_name}:{password}@{host}'
proxies = {'http': proxy_url, 'https': proxy_url}


trtProdNm = ''
# try :
for urlpage in range(1, 17) :

    row = 0
    df1 = pd.DataFrame({'상품번호':[], '카테고리':[], '브랜드명':[], '상품명':[], '가격':[], '원가격':[], '사이즈':[], '제품이미지':[]})

    baseurl = ''
    basecate = ''
    basecate2 = ''

    if urlpage == 1 : 
        baseurl = 'https://www.colognese.com/woman/?categories=accessories&page='
        basecate = 'woman > accessories > '
        basecate2 = 'accessories'
    if urlpage == 2 : 
        baseurl = 'https://www.colognese.com/woman/?categories=bags&page='
        basecate = 'woman > bags > '
        basecate2 = 'bags'
    if urlpage == 3 : 
        baseurl = 'https://www.colognese.com/woman/?categories=clothing&page='
        basecate = 'woman > clothing > '
        basecate2 = 'clothing'
    if urlpage == 4 : 
        baseurl = 'https://www.colognese.com/woman/?categories=jewellery&page='
        basecate = 'woman > jewellery > '
        basecate2 = 'jewellery'
    if urlpage == 5 : 
        baseurl = 'https://www.colognese.com/woman/?categories=shoes&page='
        basecate = 'woman > shoes > '
        basecate2 = 'shoes'
    if urlpage == 6 : 
        baseurl = 'https://www.colognese.com/man/?categories=accessories&page='
        basecate = 'man > accessories > '
        basecate2 = 'accessories'
    if urlpage == 7 : 
        baseurl = 'https://www.colognese.com/man/?categories=bags&page='
        basecate = 'man > bags > '
        basecate2 = 'bags'
    if urlpage == 8 : 
        baseurl = 'https://www.colognese.com/man/?categories=clothing&page='
        basecate = 'man > clothing > '
        basecate2 = 'clothing'
    if urlpage == 9 : 
        baseurl = 'https://www.colognese.com/man/?categories=shoes&page='
        basecate = 'man > shoes'
        basecate2 = 'shoes'
    if urlpage == 10 : 
        baseurl = 'https://www.colognese.com/kids/?categories=accessories&page='
        basecate = 'kids > accessories'
        basecate2 = 'accessories'
    if urlpage == 11 : 
        baseurl = 'https://www.colognese.com/kids/?categories=clothing&page='
        basecate = 'kids > clothing'
        basecate2 = 'clothing'
    if urlpage == 12 : 
        baseurl = 'https://www.colognese.com/kids/?categories=shoes&page='
        basecate = 'kids > shoes'
        basecate2 = 'shoes'
    if urlpage == 13 : 
        baseurl = 'https://www.colognese.com/outlet/?categories=man&page='
        basecate = 'outlet > man'
        basecate2 = 'man'
    if urlpage == 14 : 
        baseurl = 'https://www.colognese.com/outlet/?categories=kids&page='
        basecate = 'outlet > kids'
        basecate2 = 'kids'
    if urlpage == 15 : 
        baseurl = 'https://www.colognese.com/outlet/?categories=woman&page='
        basecate = 'outlet > woman'
        basecate2 = 'woman'
    if urlpage == 16 : 
        baseurl = 'https://www.colognese.com/lifestyle/'
        basecate = ''

    prodstop = 0

    for page in range(1, 30) :

        url = ''

        if urlpage != 16 : 
            url = baseurl+str(page)
        else :
            url = baseurl

        res = requests.get(url, headers=headers, proxies=proxies, verify=False)
        res.encoding='UTF-8'
        html = res.text
        soup = BeautifulSoup(html, "html.parser")

        listres = soup.find_all(class_='js-product-miniature-wrapper')

        prodrow = 0
        
        for i in listres : 
            
            print(page)

            productreference = i.find('article')['data-id-product']
            productreference = productreference.replace(' ', '')

            if trtProdNm == productreference :
                prodstop = 1
                break

            if prodrow == 0 :
                trtProdNm = productreference 

            prodrow += 1

            brand = i.find(class_='product-brand text-muted')
            if brand : 
                brand = brand.text
                brand = brand.replace(' ', '')
                brand = brand.replace('\n', '')

            prodnm = i.find(class_='h3 product-title')
            if prodnm : 
                prodnm = prodnm.text
                prodnm = prodnm.replace(' ', '')
                prodnm = prodnm.replace('\n', '')

            price = i.find('span', {'class': 'product-price'})
            if price : 
                price = price.text
                price = price.replace(' ', '')
                price = price.replace('\n', '')
                price = price.replace(',', '')
                price = price[1:]
                price = float(price)
                price = math.ceil(price)
                price = math.ceil(c.convert(price,'USD','KRW'))
                price = str(price) + '원'

            befprice = i.find('span', {'class': 'regular-price text-muted'})
            if befprice : 
                befprice = price.text
                befprice = price.replace(' ', '')
                befprice = price.replace('\n', '')
                befprice = price.replace(',', '')
                befprice = price[1:]
                befprice = float(price)
                befprice = math.ceil(price)
                befprice = math.ceil(c.convert(price,'USD','KRW'))
                befprice = str(price) + '원'

            allsize = ''
            size = i.find_all(class_='sizeValuLittle')
            for sizei in size :
                sizei = sizei.text
                sizei = sizei.replace(' ', '')
                sizei = sizei.replace('\n', '')
                allsize = allsize + ' ' + sizei

            category = i.find(class_='product-category-name text-muted')
            if category : 
                category = category.text
                category = category.replace(' ', '')
                category = category.replace('\n', '')

                if category == basecate2 :
                    category = basecate
                else :
                    category = basecate + ' > ' + category
            
            tgturl = i.find(class_='product-description-short text-muted').find('a')['href']
            resdtl = requests.get(tgturl, headers=headers, proxies=proxies, verify=False)
            resdtl.encoding='UTF-8'
            htmldtl = resdtl.text
            soupdtl = BeautifulSoup(htmldtl, "html.parser")

            imgList = soupdtl.find_all(class_='product-lmage-large')

            totimg = ''
            for img in imgList :
                
                jpg = img.find('img')['data-image-large-src']
                totimg = totimg + jpg + '\n' 

            print(tgturl, productreference, category, brand, prodnm, price, befprice, allsize, totimg)

            df1.loc[row] = [productreference, category, brand, prodnm, price, befprice, allsize, totimg]
            row += 1
            # if row == 2 : row + '22'
            # break
        if prodstop == 1 : break

            
    #     break 
    # break
# except: 
#     path = 'C:/Users/go_he/OneDrive/바탕 화면/PythonWork/colognese_except.xlsx'
#     df1.to_excel(excel_writer=path)      


    basecate = ''
    basecate2 = ''
    path = 'C:/Users/go_he/OneDrive/바탕 화면/PythonWork/colognese_' + basecate + '.xlsx'
    df1.to_excel(excel_writer=path)


