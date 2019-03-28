import sys
sys.stdin = open('B1_numbering.txt')

def isWall(x, y):
    if x < 0 or x > N-1: return True
    if y < 0 or y > N-1: return True
    return False

def BFS(x, y):
    global flag
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    visit[x][y] = cnt
    flag += 1

    for i in range(4):
        rex = x + dx[i]
        rey = y + dy[i]
        if not isWall(rex, rey):
            if data[rex][rey] == 1 and visit[rex][rey] == 0:
                BFS(rex, rey)

N = int(input())
data = [list(map(int, input())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]

cnt = 0
stack = []

for i in range(N):
    for j in range(N):
        if data[i][j] == 1 and visit[i][j] == 0:
            cnt += 1
            flag = 0
            BFS(i, j)
            stack.append(flag)
print(cnt)
for i in sorted(stack):
    print(i)
