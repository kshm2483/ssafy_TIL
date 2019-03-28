import sys
sys.stdin = open('B5_buildup.txt')

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

for i in data:
    print(i)