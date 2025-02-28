def max(a ,b) :
    max = 0
    if a > b :
        max = a
    else :
        max = b

    return max

first = int(input("첫 번째 정수를 입력하세요"))
second = int(input("두 번째 정수를 입력하세요"))

print(max(first, second))
