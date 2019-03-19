import sys
sys.stdin = open('0318_inout.txt')

data1 = int(input())
a, b = map(int, input().split())
data2 = [list(map(int, input())) for _ in range(a)]

for i in data2:
    print(*i)