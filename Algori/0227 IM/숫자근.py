# T = int(input())
# data = [input().strip() for _ in range(T)]

T = 2

data = ['991', '199']

sum = 0
max = -1
result = 0

def minsum(sum):
    while sum > 9:
        a = str(sum)
        sum = int(a[0]) + int(a[1])
    return sum

for i in range(T):
    for j in range(len(data[i])):
        sum += int(data[i][j])

    sum = minsum(sum)

    if sum > max:
        max = sum
        result = int(data[i])

    elif sum == max:
        if result > int(data[i]):
            result = int(data[i])

    sum = 0

print(result)