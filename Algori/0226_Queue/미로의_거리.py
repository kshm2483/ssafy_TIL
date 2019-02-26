def isWall(x, y):
    if x < 0 or x > N - 1: return True
    if y < 0 or y > N - 1: return True
    return False

def maze(data):
    global visited, x, y
    # delta를 위한 좌표
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]

    # Queue
    Q = []
    Q.append((x, y))
    visited[x][y] = 1
    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            rex = x + dx[i]
            rey = y + dy[i]
            if not isWall(rex, rey):
                if data[rex][rey] == 0 and visited[rex][rey] == 0:
                    Q.append((rex, rey))
                    visited[rex][rey] = visited[x][y] + 1
                elif data[rex][rey] == 3:
                    visited[rex][rey] = visited[x][y] + 1
                    return visited[rex][rey] - 2
    return 0

import sys
sys.stdin = open('미로의_거리_input.txt', 'r')

for tc in range(int(input())):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    # 확인용
    # for i in range(N):
    #     print(i, visited[i])

    # 출발점
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                x, y = i, j

    print(f'#{tc+1} {maze(data)}')