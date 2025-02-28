word = input('단어를 입력하세요. ')
word = word.lower()
s = ['a', 'e', 'i', 'o', 'u']

count = 0

for i in range(0, len(word)):
    if word[i] in s:
        count += 1


print(count)
