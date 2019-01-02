import requests
# import bs4.BeautifulSoup
from bs4 import BeautifulSoup as bts

# req = requests.get('https://www.naver.com/').text
# soup = bts(req, 'html.parser')
# rank = soup.select('#PM_ID_ct > div > div > div > div > div > ul')
# #print(kospi.text)
# for key in rank:
#     print(key.text)

# url = 'https://www.naver.com'
# req = requests.get(url).text
# soup = bts(req, 'html.parser')

# for key in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item'):
#     rank = key.select_one('.ah_r').text
#     name = key.select_one('.ah_k').text
#     print(f'{rank} {name}')

url = requests.get('https://www.naver.com/').text
soup = bts(url, 'html.parser')
rank_l = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')

for id, rank in enumerate(rank_l, 1):
    print(id, rank.text)