N = int(input())
maze = [list(map(int, input())) for _ in range(N)]
bang = list(map(int, input().split()))

# 1 아래 2 왼쪽 3 위 4 오른쪽
# 1 4 3 2
def isWall(x, y):
    if x < 0 or x > N-1: return True
    if y < 0 or y > N-1: return True
    return False

def robot(x, y):
    global maze
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    cnt = 0
    i = 0
    flag = 0
    while flag == 0:
        if i > 3:
            i = 0
        rex = x + dx[bang[i]-1]
        rey = y + dy[bang[i]-1]
        if isWall(rex, rey) == False:
            if maze[rex][rey] == 0:
                cnt += 1
                maze[x][y] = 2
                x = rex
                y = rey
            elif maze[rex][rey] == 2:
                flag = 1
                return cnt
            else:
                i += 1
        else:
            i += 1
    return cnt

print(robot(0, 0))