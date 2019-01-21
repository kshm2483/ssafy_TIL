def sequentialSearch(a, n, key):    # data, range(data), key
    i = 0
    while i < n and a[i] != key:
        i = i + 1

    if i < n : return i
    else: return -1

    # for문이 더 직관적임
    # for i in range(n):
    #     if a[i] == key:
    #         return i
    #     else: return -1
data = [4, 9, 11, 23, 2, 19, 7]
key = int(input())
print(sequentialSearch(data, len(data), key))