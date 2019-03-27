import sys
sys.stdin = open('input.txt')

def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubblesort(x):
    for i in reversed(range(len(x))):
    # for i in range(len(x)-1, -1, -1):
    # for i in range(len(x))[::-1]:
        for j in range(i):
            if x[j] > x[j+1]:
                swap(x, j, j+1)
                print(a)

for tc in range(int(input())):
    a = list(map(int, input().split()))
    bubblesort(a)
    print(*a)