import sys
sys.stdin = open('C0_도약_input.txt', 'r')

N = int(input())
data = [int(input()) for _ in range(N)]
leap = sorted(data)

cnt = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        first = leap[j] - leap[i]
        for k in range(j+1, N):
            second = leap[k] - leap[j]
            if first <= second <= first * 2:
                cnt += 1
print(cnt)