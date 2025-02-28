string = input("문자열을 입력하세요.")

counts = {"digits" : 0, "spaces" : 0, "alphas" : 0}


for i in string :
    if i.isalpha() :
        counts["alphas"] += 1
    elif i.isdigit() :
        counts["digits"] += 1
    elif i.isspace() :
        counts["spaces"] += 1


print("digits :", counts["digits"], "spaces :", counts["spaces"], "alphas :", counts["alphas"])
