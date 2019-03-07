import sys
sys.stdin = open('C4_원안의마을_input.txt', 'r')

N = int(input())
data = [list(map(int, input())) for _ in range(N)]

def findp(x, y):
    maxx = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                if abs(i-x)**2 + abs(j-y)**2 > maxx:
                    maxx = abs(i-x)**2 + abs(j-y)**2

    print(int((maxx**0.5) + (int(maxx)%(maxx**0.5) > 0)))

for i in range(N):
    for j in range(N):
        if data[i][j] == 2:
            findp(i, j)