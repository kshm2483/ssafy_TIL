import random
import requests
import json
from pprint import pprint

"""
0. random 으로 로또번호를 생성합니다.
1. API를 통해 우승 번호를 가져옵니다. (1번)
2. 0번과 1번을 비교하여 나의 등수를 알려준다.

1. url 요청 보내서 정보를 가져옵니다.
    - json으로 받는다. (딕셔너리로 접근)
2. API 의 당첨번호와 보너스 번호를 저장하고,
3. 뽑은게 몇등인지 하는거 뽑으세요. 끝?

set 은 자리가 없고, 중복허용 ㄴ

set1 & set2 교집합
set1.intersection(set2)
set1 | set2 합집합
set1.union(set2)
set1 - set2 차집합

"""
# set_mylot = set(random.sample(range(1, 46), 7))
# 랜덤 7숫자 선정
url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
req = requests.get(url)
lotto = req.json()
# 정보를 딕셔너리로 가져옴
# relot = []
# bolot = []

# bolot.append(lotto.get(f"bnusNo"))
# for i in range(1, 7):
#     relot.append(lotto.get(f"drwtNo{i}"))

# set_relot = set(relot)
# set_bolot = set(bolot)

# dang = 0
# dan2 = 0
# dan3 = 0
# dan4 = 0
# dan5 = 0
# while True:
#     set_mylot = set(random.sample(range(1, 46), 6))
#     dang += 1
#     if len(set_mylot & set_relot) == 6:
#         print("1등")
#         print(f"{dang}번 루프")
#         print(f"2등 {dan2}번 당첨")
#         print(f"3등 {dan3}번 당첨")
#         print(f"4등 {dan4}번 당첨")
#         print(f"5등 {dan5}번 당첨")
#         break
#     elif len(set_mylot & set_relot) == 5 and len(set_mylot & set_bolot) == 1:
#         dan2 += 1
#         print("2등")
#         print(f"{dang}번 루프")
#     elif len(set_mylot & set_relot) == 5:
#         dan3 += 1
#         print("3등")
#         print(f"{dang}번 루프")
#     elif len(set_mylot & set_relot) == 4:
#         dan4 += 1
#         print("4등")
#         print(f"{dang}번 루프")
#     elif len(set_mylot & set_relot) == 3:
#         dan5 += 1
#         print("5등")
#         print(f"{dang}번 루프")
#     else:
#         print(f"{dang}번 루프")


winner = []
for i in range(1, 7):
    winner.append(lotto[f"drwtNo{i}"])

bonus = lotto["bnusNo"]
print("당첨 번호: " + str(winner))
print("보너스 번호: " + str(bonus))

count = 0
co2 = 0
co3 = 0
co4 = 0
co5 = 0

while True:
    count += 1
    my_numbers = sorted(random.sample(range(1, 46), 6))
    matched = len(set(winner) & set(my_numbers))
    if matched == 6:
        print("1등")
        break
    elif matched == 5:
        if bonus in my_numbers:
            co2 += 1
            print("2등")
        else:
            co3 += 1
            print("3등")
    elif matched == 4:
        co4 += 1
        print("4등")
        print(count, "번만에 당첨")
        print("2등 당첨 횟수", co2)
        com3 = co3*1562848
        com4 = co4*50000
        com5 = co5*5000
        money = count*1000
        print("쓴돈은", money-com3-com4-com5)
        break
    elif matched == 3:
        co5 += 1
        print("5등")
    else:
        print("꽝")