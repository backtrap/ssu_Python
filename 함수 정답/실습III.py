def hap(a):
    sum = 0
    while a > 0 :
        digit = a % 10
        print(digit, end=' ')
        sum = sum + digit
        a = a // 10
        print(a, end=' ')
    return sum

a = int(input("정수를 입력하세요 "))

print(hap(a))


