# 6
# 2 -1 2 3 4 -5

A = int(input())
A_data = list(map(int, input().split()))

# 멍청한 다람쥐
stupid = 0

data_sum = A_data[0]
result = A_data[0]

for i in range(1, len(A_data)):
    data_sum = max(data_sum + A_data[i], A_data[i])
    result = max(data_sum, result)

# 똑똑한 다람쥐
smart = 0
s_cnt = 0
j = 0
while j < A:
    if A_data[j] > 0:
        smart += A_data[j]
        s_cnt += 1
    j += 1
if s_cnt == 0:
    smart = max(A_data)

print(result, smart)