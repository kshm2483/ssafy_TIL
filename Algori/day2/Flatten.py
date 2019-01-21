import sys
sys.stdin = open("input1.txt", "r")

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    dump_count = 0
    for i in range(N):
        max = 0
        min = 987654321
        for j in data:
            if j > max:
                max = j
            if j < min:
                min = j
        for k in data:
            if k == max:
                data[k] = max - 1
            if k == min:
                data[k] = min + 1

    print(max, min)
    # print('#{} {}'.format(test_case, max-min))

#import sys
#sys.stdin = open("input.txt")

T = 10

for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    for i in range(N):
        max = 0
        min = 987654321
        for i in range(len(data)):
            if max < data[i]:
                max = data[i]
                idx_max = i
            if min > data[i]:
                min = data[i]
                idx_min = i

        data[idx_max] -= 1
        data[idx_min] += 1

        max_num = 0
        min_num = 101

        for j in range(len(data)):
            if max_num < data[j]:
                max_num = data[j]
            if min_num > data[j]:
                min_num = data[j]

    print('#{} {}'.format(test_case, max_num - min_num))


def solve(data, dumpCount):
    for i in range(dumpCount):
        maxIndex = 0        # 최고높이 인덱스
        minIndex = 0        # 최저높이 인덱스
        for j in range(1, 100):
            if data[maxIndex] < data[j]: #최고 높이의 상자 찾기
                maxIndex = j
            if data[minIndex] > data[j]: #최저 높이의 상자 찾기
                minIndex = j
        data[maxIndex] -= 1     #최고 높이 감소
        data[minIndex] += 1     #최저 높이 증가

    # 반드시 최종 덤프 수행 후, 최고점과 최저점의 높이 차 반환
    # 평탄화가 끝난 이후 최고, 최저 탐색
    maxValue = data[0]
    minValue = data[0]
    for i in range(1, 100):
        if maxValue < data[i] : maxValue = data[i]
        if minValue > data[i] : minValue = data[i]

    return maxValue - minValue

import sys
sys.stdin = open("flatten_input.txt")
T = 10
for tc in range(T):
    dumpCount = int(input())
    data = list(map(int, input().split())) # 가로 길이는 100
    print("#{} {}".format(tc+1, solve(data, dumpCount)))