R = int(input())

cnt = 0
for i in range(1, R+1):
    for j in range(1, R+1):
        if i*i + j*j <= R*R:
            cnt += 1

print(cnt*4)