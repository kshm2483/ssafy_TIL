def rotate(data):
    front, rear = 0, N
    a = 0
    while a < M:
        front = (front + 1) % len(data)
        a += 1
    return data[front]

import sys
sys.stdin = open('회전_input.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    print(f'#{tc+1} {rotate(data)}')