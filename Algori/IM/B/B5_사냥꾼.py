N = int(input())
data = [list(input()) for _ in range(N)]

def isWall(x, y):
    if x < 0 or x > N-1: return True
    if y < 0 or y > N-1: return True
    return False

def hunt(x, y):
    #     상 우상 우 우하 하 좌하 좌 좌상
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    cnt = 0

    for i in range(8):
        rex = x + dx[i]
        rey = y + dy[i]
        while True:
            if isWall(rex, rey):
                break
            if data[rex][rey] == '0' or data[rex][rey] == '1':
                break
            elif data[rex][rey] == '2':
                cnt += 1
                data[rex][rey] = '3'
                rex = rex + dx[i]
                rey = rey + dy[i]
            else:
                rex = rex + dx[i]
                rey = rey + dy[i]
    return cnt

sum = 0
for i in range(N):
    for j in range(N):
        if data[i][j] == '1':
            a = hunt(i, j)
            sum += a
print(sum)