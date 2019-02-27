# T = input()
T = 4
pig = [[4, 'N'], [7, 'Y'], [5, 'N'], [6, 'Y']]
# pig = [[5, 'Y'], [6, 'Y']]

# 먹을때 최솟값
min = 10
# 안먹을때 최소값
man = 0

for i in range(T):
    if pig[i][1] == 'Y':
        if min > int(pig[i][0]):
            min = int(pig[i][0])
    else:
        if man < int(pig[i][0]):
            man = int(pig[i][0])
if min <= man:
    print('F')
elif min == 10:
    print('F')
else:
    print(min)