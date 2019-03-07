N = int(input())
data = [[0]*N for _ in range(N)]

x, y = 0, -1
num = 0
cnt = N

while num < N*N:
    # 오른
    for i in range(cnt):
        y += 1
        num += 1
        data[x][y] = num
    cnt -= 1
    # 아래
    for i in range(cnt):
        x += 1
        num += 1
        data[x][y] = num
    # 왼쪽
    for i in range(cnt):
        y -= 1
        num += 1
        data[x][y] = num
    cnt -= 1
    # 위쪽
    for i in range(cnt):
        x -= 1
        num += 1
        data[x][y] = num

for i in range(N):
    for j in range(N):
        print(data[i][j], end=' ')
    print()

