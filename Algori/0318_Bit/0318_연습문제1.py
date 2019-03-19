import sys
sys.stdin = open('0318_연습문제1.txt')

N = list(map(int, input()))

for i in range(10):
    n = 0
    for j in range(i*7, i*7+7, 1):
        n = n * 2 + N[j]
    print(n, end = ' ')
print()