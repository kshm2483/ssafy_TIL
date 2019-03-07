N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
gakgi = [[0]*N for _ in range(N)]
gakdo = []

while True:
    gakdo.append(int(input()))
    if gakdo[-1] == 0:
        break

def gak90():
    for i in range(N):
        for j in range(N):
            gakgi[i][j] = data[i][j]
    return

# def gak180():
#
#     return
#
# def gak270():
#
#     return

for i in range(len(gakdo)):
    if gakdo[i] == 90:
        gak90()
    # elif gakdo[i] == 180:
    #     gak180()
    # elif gakdo[i] == 270:
    #     gak270()
    # else:

for i in range(N):
    print(i, gakgi[i])