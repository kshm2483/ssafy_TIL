import sys
sys.stdin = open("sample4_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    max = 0
    min = 987654321
    for i in range((N-M)+1):
        sum = 0
        for j in range(M):
            sum = sum + data[i+j]
        if sum > max:
            max = sum
        if sum < min:
            min = sum
    result = max - min

    print("#{} {}".format(test_case, result))


    max = -987654321
    min = 987654321

    # 1.
    # for i in range(N-M+1):  # 리스트를 넘지 않는 범위까지만 탐색
    #     sum = 0    # 초기화 위치
    #     for j in range(M):  # 더할 값 범위
    #         sum = sum + data[i+j]   # data[i+j]
    #     if sum > max: max = sum
    #     if sum < min: min = sum