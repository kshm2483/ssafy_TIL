import sys
sys.stdin = open('B8_연속부분최대곱_input.txt', 'r')

N = int(input())
data = [float(input()) for _ in range(N)]

# 1중 루프
result = [data[0]]
for i in range(1, len(data)):
    if result[-1] * data[i] > data[i]:
        result.append(result[-1] * data[i])
    else:
        result.append(data[i])

print('{:.3f}'.format(max(result)))


# 2중 루프
# mul = 1.0
# max = 0.0
#
# for i in range(N):
#     mul = 1.0
#     for j in range(i, N):
#         mul *= data[j]
#         if mul > max:
#             max = mul
# print('{:.3f}'.format(max))