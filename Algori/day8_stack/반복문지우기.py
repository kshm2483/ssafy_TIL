import sys
sys.stdin = open('반복문지우기_input.txt', 'r')

T = int(input())

def bock(text):
    global s
    for i in text:
        if len(s) == 0:
            s.append(i)
        elif s[-1] != i:
            s.append(i)
        else:
            s.pop()
    return len(s)

for tc in range(T):
    text = input()
    s = []
    print(f'#{tc+1} {bock(text)}')