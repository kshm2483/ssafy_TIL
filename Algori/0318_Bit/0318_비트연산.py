# 비트연산 예제 2
def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
    print(output, end=' ')

a = 0x10
x = 0x01020304

print('%d = '%a, end='')
Bbit_print(a)
print()

print('0%x = '%x, end='')
for i in range(0, 4):
    Bbit_print((x >> i*8) & 0xff)
print()

# 비트연산 예제 3 / endian
n = 0x00111111

if n & 0xff:
    print('little endian')
else:
    print('big endian')

# 비트연산 예제 5
def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
    print(output)

a = 0x86
key = 0xAA
print(bin(a))
print('a      ==> ', end='')
Bbit_print(a)
print('a^=key ==> ', end='')
a ^= key
Bbit_print(a)
print('a^=key ==> ', end='')
a ^= key
Bbit_print(a)