def max_and_min(n1, n2, n3) :
    l = [n1, n2, n3]
    
    l2 = sorted(l)

    print("가장 큰 수 :", l2[2])
    print("가장 작은 수 :", l2[0])

k = input("3 수를 입력하시오 : ")
h = k.split()
n1 = int(h[0])
n2 = int(h[1])
n3 = int(h[2])

max_and_min(n1, n2, n3)
