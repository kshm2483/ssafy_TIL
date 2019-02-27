# np = [[3, 7], [15, 7], [5, 2]]

T = int(input())
np = [list(map(int, input().split())) for _ in range(T)]

bp = [[0]*100 for _ in range(100)]

cnt = 0

while np:
    x, y = np.pop(0)
    for i in range((90-y), (100-y)):
        for j in range(x, (x+10)):
            bp[i][j] = 1

for i in range(100):
    for j in range(100):
        if bp[i][j] == 1:
            cnt += 1
print(cnt)