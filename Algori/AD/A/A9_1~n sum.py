def DFS(i):
    global sums
    if i < 1: return
    sums += i
    DFS(i-1)

N = int(input())
sums = 0
DFS(N)
print(sums)