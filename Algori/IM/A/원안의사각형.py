R = int(input())

cnt = 0

for i in range(R):
    for j in range(R):
        if (R-i) ** 2 + (R-j) **2 <= R ** 2:
            cnt += 1

print(cnt*4)