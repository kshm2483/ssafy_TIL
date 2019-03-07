N = 5
data = [list(map(int, input().split())) for _ in range(N)]
ans = [list(map(int, input().split())) for _ in range(N)]

def erager(num):
    global cnt
    for i in range(N):
        for j in range(N):
            if data[i][j] == num:
                cnt += 1
                data[i][j] = 0
                return
def matc():
    bingo = 0
    lcsum, rcsum = 0, 0
    for i in range(N):
        rsum, csum = 0, 0
        for j in range(N):
            rsum += data[i][j]
            csum += data[j][i]
        lcsum += data[i][i]
        rcsum += data[i][N-i-1]
        if rsum == 0: bingo += 1
        if csum == 0: bingo += 1
    if lcsum == 0: bingo += 1
    if rcsum == 0: bingo += 1
    if bingo >= 3: return True
    else: return False

cnt = 0
flag = 0
for i in range(N):
    for j in range(N):
        erager(ans[i][j])
        if matc():
            flag = 1
            break
    if flag: break

print(cnt)