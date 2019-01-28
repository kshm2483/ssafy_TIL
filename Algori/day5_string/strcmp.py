def strcmp(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
    return True

def strcmp(str1, str2):
    i = 0
    if len(str1) != len(str2):
        return False
    else:
        while i < len(str1):
            if str1[i] != str2[i]:
                return False
            i += 1
    return True

a = 'abc'
b = 'abc'

print(strcmp(a, b))