N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

def findz(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    result = []

    for i in range(4):
        count = 1
        rex = x + dx[i]
        rey = y + dy[i]
        while True:
            if data[rex][rey] == 0:
                result.append(count)
                break
            else:
                rex += dx[i]
                rey += dy[i]
                count += 1
    return result

for i in range(1, N-1):
    for j in range(1, N-1):
        if data[i][j] == 1:
            a = findz(i, j)
            data[i][j] = min(a)

sum = 0
for i in range(N):
    for j in range(N):
        sum += data[i][j]

print(sum)