inFp = None     # 입력 파일
inStr = ""	# 읽어온 문자열

inFp = open("C:/Temp/data1.txt", "r", encoding="UTF-8")

while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    print(inStr, end = "")

inFp.close()
