import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    max = 0
    min = 987654321
    for i in range(len(data)):
        if data[i] > max:
            max = data[i]
        if data[i] < min:
            min = data[i]
    result = max - min
    print("#{} {}".format(test_case, result))

#  강사님 답
# 1.
# for test_case in range(1, T + 1):
#     N = int(input())
#     data = list(map(int, input().split()))
#     max = -987654321
#     min = 987654321
#     for i in range(N):
#         if min > data[i]:
#             min = data[i]
#         if max < data[i]:
#             max = data[i]
#
#     result = max - min
#     print("#{} {}".format(test_case, result))

# 2.
# 초기값을 리스트의 0번째로 넣어서 비교가능
#     max = data[0]
#     min = data[0]
#     for i in range(1, N):
#         if min > data[i]:
#             min = data[i]
#         if max < data[i]:
#             max = data[i]

