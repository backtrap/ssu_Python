def makeDict(key, val) :

    result = dict()
    result[key] = val

    return result

first = input("키를 입력하세요")
second = input("값을 입력하세요")


print(makeDict(first, second))