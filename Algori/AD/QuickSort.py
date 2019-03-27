import sys
sys.stdin = open('input.txt')

def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def Qsort(s, e):
    if s >= e: return
    # P pivot T target
    P , T = e, s
    for L in range(s, e):
        if a[L] < a[P]:
            swap(a, L, T)
            T += 1
    swap(a, P, T)
    print(a)
    Qsort(s, T-1)
    Qsort(T+1, e)

for tc in range(int(input())):
    a = list(map(int, input().split()))
    Qsort(0, len(a)-1)
    print(a)