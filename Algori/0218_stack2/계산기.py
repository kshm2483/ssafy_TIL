str1 = '2+3*4/5'
str2 = ''
stack1 = []

soonseo = {'(':0,
           '+':1, '-':1,
           '*':2, '/':2
           }

for i in str1:
    if i.isdigit():
        str2 += i
    else:
        stack1.append(i)

    # elif soonseo[stack1[-1]] != soonseo[i]:
    #     stack1.append(i)
    # elif soonseo[stack1[-1]] == soonseo[i]:
    #     str2 += stack1[-1]
    #     stack1.append(i)

print(str2, stack1)