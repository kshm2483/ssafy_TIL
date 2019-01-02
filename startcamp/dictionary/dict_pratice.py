"""
파이선 dictionary 활용 기초!
"""
# dict = {
#     "대전" : 23,
#     "서울" : 30,
#     "구미" : 20
# }
# print(type(dict.values()))

# list = [1, 231, "123124124"]
# print(len(list))

# 1. 평균을 구하세요.

# 1-1.
# score = {
#     "국어" : 87,
#     "영어" : 92,
#     "수학" : 40
# }
# total = 0
# for i in score.values():
#     total += i
# print(total/len(score))

# # 1-2.
# deohagi = sum(score.values())
# print(deohagi/len(score))

# # 2. 반 평균을 구하시오

# scores = {
#     "철수" : {
#         "수학" : 80,
#         "국어" : 90,
#         "음악" : 100
#     },
#     "영희" : {
#         "수학" : 70,
#         "국어" : 60,
#         "음악" : 50
#     }
# }
# total = 0
# count = 0

# for i in scores.values():
#     for j in i.values():
#         count += 1
#         total += j
# print(total/count)

# 3 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# scores = {
#     "국어" : 87,
#     "영어" : 92,
#     "수학" : 40
# }
# for key, value in scores.items():
#     print(key)
#     print(value)

# 3 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}

hot = 0
cold = 0
hot_city = ""
cold_city = ""
count = 0

for name, temp in cities.items():
    # name = "서울"
    # temp = [-6, -10, 5]
    if count == 0:
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    # else:
    #     # 최저 온도가  cold 보다 더 추우면, cold  에 넣고
    #     if min(temp) < cold:
    #         cold = min(temp)
    #         cold_city = name
    #     # 최고 온도가 hot 보다 더 더우면, hot  에 넣고
    #     if max(temp) > hot:
    #         hot = max(temp)
    #         hot_city = name
    count += 1

print(f"{hot_city}, {cold_city}")