name = input("email을 입력하세요.")

if len(name.split("@", 2)) < 2 :
    print("email 형식이 아닙니다.")
else :
    k = name.split("@", 2)

    print("id :", k[0])

    print("domain :", k[1])
