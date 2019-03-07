import sys
sys.stdin = open('B9_덧셈_input.txt', 'r')

S, X = map(str, input().split())

# 2개의 정수로 분리
# for i in range(1, len(S)):
#     A = int(S[:i])
#     B = int(S[i:])
#     if A + B == int(X):
#         print('{}+{}={}'.format(A, B, X))

# 3개의 정수로 분리
for i in range(1, len(S)):
    A = int(S[:i])
    for j in range(i+1, len(S)):
        B = int(S[i:j])
        C = int(S[j:])
        print(A, B, C)