def bruteForce(p, t):
    M = len(p)
    N = len(t)
    i, j = 0, 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = - 1
        i = i + 1
        j = j + 1
    if j == M:
        return i - M
    else:
        return -1

def bruteForce2(text, pattern):
    for i in range(len(text)-len(pattern)+1):
        cnt = 0
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
            else: cnt += 1
        if (cnt >= len(pattern)) : return i
    return -1

text = 'This is book. This is a computer'
pattern = 'is'

print(bruteForce2(text, pattern))
print(text.find(pattern))
print(text.count(pattern))