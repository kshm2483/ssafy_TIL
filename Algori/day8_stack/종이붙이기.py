import sys
sys.stdin = open('종이붙이기_input.txt', 'r')

T = int(input())

def ori(n):
    if n == 1:return 1
    if n == 2:return 3
    else:
        return ori(n-1) + (2*ori(n-2))

for tc in range(T):
    N = int(input())
    print(f'#{tc+1} {ori(N/10)}')