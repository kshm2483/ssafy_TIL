import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

kospi = soup.select_one('#KOSPI_now')
print(kospi.text)


# req = requests.get("https://www.google.com")
# soup = BeautifulSoup(req, 'html.parser')
# kospi = soup.select_one('경로')

# print(req)
# print(req.text)
# print(req.status_code)