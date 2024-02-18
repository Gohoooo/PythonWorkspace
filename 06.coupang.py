#가끔 브라이트에서 오류 뱉을시 메일가서 증명

from bs4 import BeautifulSoup
import requests
import warnings
import csv

warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

host = 'brd.superproxy.io:22225'
user_name = 'brd-customer-hl_111b508b-zone-unblocker'
password = 'z8l9602yshyy'
proxy_url = f'https://{user_name}:{password}@{host}'

proxies = {'http': proxy_url, 'https': proxy_url}

# print(proxy_url)

keyword = input('제품 입력 : ') 
# keyword = '노트북'
# url = f'https://www.coupang.com/np/search?component=&q={keyword}'

link_list = []
with open(f"coupang_{keyword}.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["제품명", "가격", "링크"])
    for page_num in range(1, 3) :
        # print(f"<<<<<<<{page_num}페이지>>>>>>")

        url = f'https://www.coupang.com/np/search?rocketAll=false&searchId=f3d6e40bcd7a465ca141285e427c7716&q={keyword}&page={page_num}&listSize=36'
        res = requests.get(url, proxies=proxies, verify=False)
        html = res.text
        soup = BeautifulSoup(html, "html.parser")
        items = soup.select("[class=search-product]")

        for item in items : 
            name = item.select_one(".name").text
            price = item.select_one(".price-value")
            if not price:
                continue
            else : price = price.text

            link = f"https://www.coupang.com{item.a['href']}"

            link_list.append(link)

            writer.writerow([name, price, link])


        # print(f"{name} : {price.text}")
        # print(link)
        # print()

# print(link_list)
# print(len(link_list))

with open(f"coupang_{keyword}_detail_page.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["브랜드", "제품명", "현재 판매가", "회원 판매가", "옵션", "상세정보", "url"])
    for url in link_list :
        res = requests.get(url, proxies=proxies, verify=False)
        html = res.text
        soup = BeautifulSoup(html, "html.parser")

        brand = soup.select_one(".prod-brand-name").text.strip()
        title = soup.select_one(".prod-buy-header__title").text.strip()

        prod_sale_price   = soup.select_one(".prod-sale-price")
        prod_coupon_price = soup.select_one(".prod-coupon-price")

        if prod_sale_price : 
            prod_sale_price = prod_sale_price.select_one(".total-price").text.strip()
        else : prod_sale_price = ""

        if prod_coupon_price : 
            prod_coupon_price = prod_coupon_price.select_one(".total-price").text.strip()
        else : prod_coupon_price = ""

        print(f"브랜드 : {brand}, 제품명 : {title}, 현재 판매가 : {prod_sale_price}, 회원 판매가 : {prod_coupon_price}")

        prod_option_item = soup.select(".prod-option-item") # 옵션

        if prod_option_item :
            option_list = []
            for item in prod_option_item :
                title = item.select_one(".title").string.strip()
                value = item.select_one(".value").string.strip()
                option_list.append(f"{title} : {value}")
            prod_option_item = ", ".join(option_list)
            # print(prod_option_item)
        else : 
            prod_option_item = ""

        prod_description = soup.select(".prod-description .prod-attr-item") # 상세정보

        if prod_description : 
            description_list = []
            for description in prod_description : 
                description_list.append(description.string.strip())

            prod_description = ", ".join(description_list)
            print(prod_description)
        else : 
            prod_description = ""

        writer.writerow([brand, title, prod_sale_price, prod_coupon_price, prod_option_item, prod_description, url])

        print()




