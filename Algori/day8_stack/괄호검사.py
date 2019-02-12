import sys
sys.stdin = open('괄호검사_input.txt', 'r')

T = int(input())

def stack(text):
    s = []
    for i in text:
        if i == '(' or i == '{':
            s.append(i)
        elif i == ')':
            if len(s) == 0:
                return 0
            elif s[-1] != '(':
                return 0
            else:
                s.pop()
        elif i == '}':
            if len(s) == 0:
                return 0
            elif s[-1] != '{':
                return 0
            else:
                s.pop()
    if len(s) == 0:
        return 1
    return 0

for tc in range(T):
    N = input()
    print(f'#{tc+1} {stack(N)}')
