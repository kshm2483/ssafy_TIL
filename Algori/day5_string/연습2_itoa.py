def itoa(numbers):
    result = []
    while numbers > 0:
        result.append(chr(numbers%10 + ord('0')))
        numbers = numbers // 10
    return ''.join(reversed(result))

print(itoa(123), type(itoa(123)))

# chr(65) # 문자로 리턴