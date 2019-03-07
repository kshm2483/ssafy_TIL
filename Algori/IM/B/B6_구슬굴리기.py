r, c = map(int, input().split())
data = [list(input()) for _ in range(c)]
N = int(input())
bang = list(map(int, input().split()))

# 1 위 2 아래 3 왼쪽 4 오른쪽
# 2 4 1 3 2 4 1 3

def isWall(x, y):
    if x < 0 or x > c-1: return True
    if y < 0 or y > r-1: return True
    return False

def marble(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    k = 0
    cnt = 1

    while k < len(bang):

        rex = x + dx[bang[k] - 1]
        rey = y + dy[bang[k] - 1]

        if isWall(rex, rey) == False:
            if data[rex][rey] == '0' or data[rex][rey] == '2':
                data[rex][rey] = '3'
                cnt += 1
                x = rex
                y = rey
            elif data[rex][rey] == '3':
                x = rex
                y = rey
            else:
                k += 1
        else:
            k += 1
    return cnt

for i in range(c):
    for j in range(r):
        if data[i][j] == '2':
            data[i][j] = '3'
            result = marble(i, j)

print(result)