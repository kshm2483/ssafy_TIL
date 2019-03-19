import sys
sys.stdin = open('0318_단순2진.txt')

code = [[0,0,0,1,1,0,1],
        [0,0,1,1,0,0,1],
        [0,0,1,0,0,1,1],
        [0,1,1,1,1,0,1],
        [0,1,0,0,0,1,1],
        [0,1,1,0,0,0,1],
        [0,1,0,1,1,1,1],
        [0,1,1,1,0,1,1],
        [0,1,1,0,1,1,1],
        [0,0,0,1,0,1,1]]

def findp(x, y):
    global M, result
    for i in range(10):
        cnt = 0
        for j in range(6, -1, -1):
            if (y-6)+j < 0: return 0
            if data[x][(y-6)+j] == code[i][j]:
                cnt += 1
            else:
                break
        if cnt == 7:
            result.append(i)
            return 7
    return 0

def verifi(ans):
    global flag
    sumod = 0
    sumev = 0
    for i in range(len(ans)):
        if i%2 == 1:
            sumod += ans[i]
        else:
            sumev += ans[i]
    if not ((sumev * 3) + sumod) % 10:
        return sumod + sumev
    return 0

for tc in range(int(input())):
    N, M = map(int, input().split())
    data = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        result = []
        idx = M - 1
        while idx > 0:
            a = findp(i, idx)
            if a == 0:
                idx -= 1
            else:
                idx -= a
        if len(result) == 8:
            a = verifi(result[::-1])
            print('#{} {}'.format(tc+1, a))
            break