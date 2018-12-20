import requests
from bs4 import BeautifulSoup as bts

url = requests.get("https://m.stock.naver.com/marketindex/index.nhn").text
soup = bts(url, 'html.parser')


for key in soup.select('.exchg_on'):
    name = key.select_one('.stock_dn').text
    # doll = key.select_one('.stock_price').text
    # gap = key.select_one('.gap_wrp').text
    print(f'{name}')