def isDecimal(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input('숫자를 입력하세요 : '))
a = isDecimal(num)

if a == True:
    print('%d는(은) 소수이다.' %num)
else:
    print('%d는(은) 소수가 아니다.' %num)
