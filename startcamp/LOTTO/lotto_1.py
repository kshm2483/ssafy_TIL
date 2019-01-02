from bs4 import BeautifulSoup
import requests
import random

numbers = random.sample(range(800, 838), 8)

# 1. lotto
for rannum in numbers:
    count = 0
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={rannum}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, "html.parser")

    lucky = soup.select(".ball_645")
    print(f"{rannum}회차 당첨번호")

    for i in lucky:
        print(i.text, end = " ")
        count += 1 
        if count == 6:
            print("+ ", end = "")
    print()
