def para_func(*para):
   result = 0
   for num in para:
      result += num
   return result

print("매개변수가 2개인 함수를 호출한 결과 ==> %s" %para_func(15,15))
print("매개변수가 10개인 함수를 호출한 결과 ==> %s" %para_func(55, 55, 55, 55, 55, 55, 55, 55, 55, 55))