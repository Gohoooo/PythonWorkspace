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

row = 0
df1 = pd.DataFrame({'Name':[], 'Career':[], 'Usage Date':[], 'created':[], 'Review_title':[], 'Review_content':[], 'Pros':[], 'Cons':[]
                  , 'Overall_rating':[], 'Value for money':[], 'Ease of use':[], 'Features':[], 'Customer support':[], 'likelihood_to_recommend':[]})

# Name : a['user_info']['full_name']
# Career : a['user_info']['company_industry']
# Usage Date : a['user_info']['time_used']
# created : a['created']
# Review_title : a['title']
# Review_content : a['content']
# Pros : a['pros']
# Cons : a['cons']
# Overall_rating : a['rating']['total_rounded']
# Value for money : a['rating']['by_field']['rating_value']
# Ease of use : a['rating']['by_field']['rating_ease']
# Features : a['rating']['by_field']['rating_features']
# Customer support : a['rating']['by_field']['rating_support']
# likelihood_to_recommend : a['rating']['by_field']['likelihood_to_recommend']

for page_num in range(1, 101) :

    url = f'https://www.getapp.com/website-ecommerce-software/a/paypal/reviews/?sort_by=most_recent&page={page_num}'
    res = requests.get(url, proxies=proxies, verify=False)
    html = res.text
    soup = BeautifulSoup(html, "html.parser")

    listRes = soup.find('script', {'id':'__NEXT_DATA__'}).text

    # print(type(listRes))
    json_object = json.loads(listRes)
    # print(type(json_object))
    # print(json_object["props"]['pageProps']['reviewsData']['reviews'])
    # print(listRes['props'])

    for a in json_object["props"]['pageProps']['reviewsData']['reviews'] :

        df1.loc[row] = [a['user_info']['full_name']
                      , a['user_info']['company_industry']
                      , a['user_info']['time_used']
                      , a['created']
                      , a['title']
                      , a['content']
                      , a['pros']
                      , a['cons']
                      , a['rating']['total_rounded']
                      , a['rating']['by_field']['rating_value']
                      , a['rating']['by_field']['rating_ease']
                      , a['rating']['by_field']['rating_features']
                      , a['rating']['by_field']['rating_support']
                      , a['rating']['by_field']['likelihood_to_recommend']]
        row += 1

df1.to_excel(excel_writer='C:/Users/go_he/OneDrive/바탕 화면/PythonWork/GetApp_Paypal.xlsx')
    





