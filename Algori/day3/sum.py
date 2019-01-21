import sys
sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    N = input()
    arr = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))

    max = -987654321
    # 행
    for x in range(len(arr)):
        sum = 0
        for y in range(len(arr[x])):
            sum += arr[x][y]
        if max < sum:
            max = sum
    # 열
    for y in range(len(arr[0])):
        sum = 0
        for x in range(len(arr)):
            sum += arr[x][y]
        if max < sum:
            max = sum
    # 대각선 1
    sum = 0
    for i in range(len(arr)):
        sum += arr[i][i]
        if max < sum:
            max = sum
    # 대각선 2
    for i in range(-1, len(arr), -1):
        sum += arr[i][i]
        if max < sum:
            max = sum
    print(f'#{test_case} {max}')