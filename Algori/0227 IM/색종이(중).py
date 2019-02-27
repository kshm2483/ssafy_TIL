# T = int(input())
# np = [list(map(int, input().split())) for _ in range(T)]

np = [[3, 7], [5, 2], [15, 7], [13, 14]]
bp = [[0]*100 for _ in range(100)]

cnt = 0

while np:
    x, y = np.pop(0)
    for i in range((90-y), (100-y)):
        for j in range(x, (x+10)):
            bp[i][j] = 1

for i in range(0, 100):
    for j in range(0, 100):
        if bp[i][j] != bp[i][j-1]:
            cnt += 1
        if bp[i][j] != bp[i-1][j]:
            cnt += 1

print(cnt)