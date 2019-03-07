import sys
sys.stdin = open('D6_회전_input.txt', 'r')

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
gakdo = []

while True:
    gakdo.append(int(input()))
    if gakdo[-1] == 0:
        break

for i in range(n):
    print(data[i])
print(gakdo)