import sys
sys.stdin = open('C3_과수원_input.txt', 'r')

N = int(input())
data = [list(input()) for _ in range(N)]

result = 0

def apple(x, y):
    sum = []
    cnt = 0
    for i in range(x+1):
        for j in range(y+1):
            if data[i][j] == '1':
                cnt += 1
    sum.append(cnt)

    cnt = 0
    for i in range(x+1):
        for j in range(y+1, N):
            if data[i][j] == '1':
                cnt += 1
    sum.append(cnt)

    cnt = 0
    for i in range(x+1, N):
        for j in range(y+1):
            if data[i][j] == '1':
                cnt += 1
    sum.append(cnt)

    cnt = 0
    for i in range(x+1, N):
        for j in range(y+1, N):
            if data[i][j] == '1':
                cnt += 1
    sum.append(cnt)

    for i in range(len(sum)):
        if sum[i] != sum[0]:
            return 0
    return 1

for i in range(N):
    for j in range(N):
        result += apple(i, j)

if result == 0:
    print(-1)
else:
    print(result)