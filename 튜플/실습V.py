#1_1
evens = [even * 2 for even in range(10)]
print(evens)

#1_2
A = ['사과', '귤', '배']
B = ['블루베리', '자몽', '아보카도']
pairs = [(a,b) for a in A for b in B if a!=b]
print(pairs)

print(pairs)

#1_3
triple_dic = {x:x**3 for x in (2, 3, 4)}
print(triple_dic)
