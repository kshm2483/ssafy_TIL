import sys
sys.stdin = open('A1_repack.txt')

def Bubble():
    global ans
    for k in range(N-1):
        for i in range(k, k+2):
            for j in range(i+1, N):
                if candy[i] > candy[j]:
                    candy[i], candy[j] = candy[j], candy[i]
        candy[k+1] += candy[k]
        ans += candy[k+1]

def InSort(arr):
    global ans
    for k in range(1, N):
        arr[k] += arr[k-1]      # K, K+1 번째 포장
        ans += arr[k]           # 포장 누계
        temp = arr[k]
        for i in range(k+1, N):
            if arr[i] < temp:   # 크거나 같을때까지 교환
                arr[i], arr[i-1] = arr[i-1], arr[i]
            else:
                break

N = int(input())
candy = list(map(int, input().split()))
ans = 0
# Bubble()
InSort(candy)
print(ans)



