str1 = '2+3*4/5'
stack1 = []

for i in str1:
    if i.isdigit():
        print(i, end='')
    else:
        stack1.append(i)

while stack1:
    print(stack1.pop(), end='')