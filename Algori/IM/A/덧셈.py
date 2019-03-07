A, SB = input().split()
SA = [*A]
N = len(SA)-1
sum = 0

for i in range(len(SA)):
    sum += int(SA[i])

print(N)
print(SA, SB)