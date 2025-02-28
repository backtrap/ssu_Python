contacts = {}

while True :
    mode = input("1) 전화번호 저장, 2) 전화번호 검색 ")
    if mode == "1" :
        name = input("저장할 사용자의 이름을 입력하세요. ")
        tel = input("전화번호를 입력하세요. ")
        contacts[name] = tel
    else :
        name = input("검색할 사용자의 이름을 입력하세요. ")
        print(contacts.get(name, "존재하지 않는 사용자 입니다."))