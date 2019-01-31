import requests
from bs4 import BeautifulSoup

# 검색할 주소
url = 'http://www.op.gg/summoner/userName='
# 검색할 text
username = 'hide on bush'
# text 가공
response = requests.get(url+username).text
soup = BeautifulSoup(response, 'html.parser')
# id값 찾아서 가져옴
wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
loses = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
# text값만 프린트
print(wins.text)
print(loses.text)