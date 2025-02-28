dict = {"one" : "하나", "two" : "둘", "three" : "셋", "four" : "넷"}

word = input("단어를 입력하세요.")

print(dict.get(word,"없는 단어 입니다."))
