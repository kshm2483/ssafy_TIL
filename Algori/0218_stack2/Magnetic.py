def magnetic(data):
    global cnt, size

    for x in range(size):
        stack = False
        for y in range(size):
            if data[y][x] == 1:
                stack = True
            if data[y][x] == 2 and stack:
                cnt += 1
                stack= False
    return cnt

# def magnetic(data):
#     global cnt, size
#
#     for x in range(size):
#         stack = []
#         for y in range(size):
#             if data[y][x] != 0:
#                 stack.append(data[y][x])
#         for i in range(len(stack)-1):
#             if stack[i:i+2] == [1, 2]:
#                 cnt += 1
#     return cnt

import sys
sys.stdin = open('마그네틱_input.txt', 'r')

T = 10
for test_case in range(T):
    cnt = 0
    size = int(input())
    table = [list(map(int, input().split())) for _ in range(size)]
    print(f'#{test_case+1} {magnetic(table)}')