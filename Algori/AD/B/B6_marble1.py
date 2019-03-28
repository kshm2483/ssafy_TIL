def DFS(n, k):
    if n == k:
        for i in range(N):
            print(marble[i]*(i+1), end=' ')
        print()
        return
    else:
        marble[k] = 1
        DFS(n, k+1)
        marble[k] = 0
        DFS(n, k+1)

N = 3
marble = [1, 2, 3]
DFS(3, 0)