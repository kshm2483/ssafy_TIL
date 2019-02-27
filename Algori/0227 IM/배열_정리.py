# Y, X = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(Y)]

Y, X = 4, 4
data = [[0,1,0,0],
        [1,1,0,1],
        [1,0,1,0],
        [1,1,1,0]]


for i in range(Y):
    for j in range(X):
        if data[i][j] == 1:
            if data[i][j-1] != 0 and (j-1) >= 0:
                data[i][j] = data[i][j-1] + 1
        print(data[i][j], end=' ')
    print()