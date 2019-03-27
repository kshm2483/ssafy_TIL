import sys
sys.stdin = open('input.txt')

def MSort(s, e):
    if s >= e: return
    m = (s+e)//2
    MSort(s, m)
    MSort(m+1, e)
    l, r, t = s, m+1, s

    while l <= m and r <= e:
        if a[l] < a[r]:
            temp[t] = a[l]
            t += 1
            l += 1
        else:
            temp[t] = a[r]
            t += 1
            r += 1
    while l <= m:
        temp[t] = a[l]
        t += 1
        l += 1
    while r <= e:
        temp[t] = a[r]
        t += 1
        r += 1
    for i in range(s, e+1):
        a[i] = temp[i]


for tc in range(int(input())):
    a = list(map(int, input().split()))
    temp = [0]*len(a)
    MSort(0, len(a)-1)
    print(temp)
    print(a)