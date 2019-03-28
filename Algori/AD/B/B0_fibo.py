memo = {1:1, 2:1}
def fib(n):
    if n == 0:
        return 0
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

N = int(input())
print(fib(N))