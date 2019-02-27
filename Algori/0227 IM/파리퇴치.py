def findx(x, y):
    global N
    cnt = -1
    for i in range(M):
        cnt += 1
    return cnt

def findy(x, y):
    global cnt
    cnt = -1
    for i in range(M):
        cnt += 1
    return cnt

def debug(x, y, dx, dy):
    global sum
    for i in range(M):
        for j in range(M):
            sum += bug[x+i][y+j]
    return sum

def findbug(data):
    global max, sum
    global N, M
    for i in range(N-M+1):
        for j in range(N-M+1):
            a = findx(i, j)
            b = findy(i, j)
            debug(i, j, a, b)
            if sum > max:
                max = sum
            sum = 0

    return max


import sys
sys.stdin = open('파리퇴치_input.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    bug = [list(map(int, input().split())) for _ in range(N)]

    max = -1
    sum = 0
    findbug(bug)

    print(f'#{tc+1} {max}')