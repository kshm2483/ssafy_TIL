a, b = map(int, input().split())

prime = [0 for _ in range(b)]

for i in range(a, b):
    if i*i > b:
        break
    if prime[i]:
        continue
    for j in range(i*2, b, i):
        prime[j] = 1

min = 9999999
max = -1
cnt = 0
for i in range(2, len(prime)):
    if prime[i] == 0:
        cnt += 1
        if min > i:
            min = i
        if i > max:
            max = i

print(cnt)
print(min+max)