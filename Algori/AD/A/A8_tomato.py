import sys
sys.stdin = open('A8_tomato.txt')

def isWall(x, y):
    if x < 0 or x > N-1: return True
    if y < 0 or y > M-1: return True
    return False

def BFS():
    global mind
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    Q = []

    for i in range(len(tomato)):
        Q.append((tomato[i][0], tomato[i][1]))
        visited[tomato[i][0]][tomato[i][1]] = 1

    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            rex = x + dx[i]
            rey = y + dy[i]
            if not isWall(rex, rey):
                if data[rex][rey] == 0 and visited[rex][rey] == 0:
                    Q.append((rex, rey))
                    visited[rex][rey] = visited[x][y] + 1
                if data[rex][rey] == 1 or data[rex][rey] == -1:
                    visited[rex][rey] = 1
    maxd = 1

    for i in range(N):
        for j in range(M):
            if visited[i][j] > maxd:
                maxd = visited[i][j]

    if maxd != 1:
        if mind > maxd:
            mind = maxd


M, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

tomato = []
flag, cnt = 0, 0
mind = 9999


for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            tomato.append((i, j))
        elif data[i][j] == -1:
            cnt += 1

if M * N == len(tomato) + cnt:
    print(0)
else:
    BFS()
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                flag = 1
if flag:
    print(-1)
else:
    print(mind-1)