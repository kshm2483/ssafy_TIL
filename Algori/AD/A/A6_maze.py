import sys
sys.stdin = open('A6_maze.txt')

def isWall(x, y):
    if x < 0 or x > Y-1: return True
    if y < 0 or y > X-1: return True
    return False

def escape(x, y):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    Q = []
    Q.append((x, y))
    visit[x][y] = 1

    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            rex = x + dx[i]
            rey = y + dy[i]
            if not isWall(rex, rey):
                if maze[rex][rey] == 0 and visit[rex][rey] == 0:
                    Q.append((rex, rey))
                    visit[rex][rey] = visit[x][y] + 1

X, Y = map(int, input().split())
sx, sy, ex, ey = map(int, input().split())
maze = [list(map(int, input())) for _ in range(Y)]
visit = [[0]*X for _ in range(Y)]

escape(sy-1, sx-1)

print(visit[ey - 1][ex - 1] - 1)