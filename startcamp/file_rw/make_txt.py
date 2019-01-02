# f = open('new2.txt', 'w', encoding='utf-8')
# for i in range(1,5):
#     data = f'{i}번째\t'
#     f.write(data)
# f.close()

# with open('new2.txt', 'w', encoding='utf-8') as f:
#     for i in range(1, 10): # 메모리 효율성을 위해 range사용
#         f.write(f'{i}번째\t')

with open('new.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())