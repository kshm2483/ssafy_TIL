a = '(((('
b = '()()()(((())()'
#120
c = ')(()()())((('
#100

for i in range(len(a)):

print(sum)

sum = 0
stack = []

T = input()

for i in range(len(T)):
    if not stack:
        stack.append(T[i])
        sum += 10
    elif stack[-1] == T[i]:
        sum += 5
        stack.append(T[i])
    else:
        sum += 10
        stack.append(T[i])