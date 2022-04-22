alphabet = "abcdefghijklmnopqrstuvwxyz"
word = str(input())

for i in alphabet:
    if i in word:
        print(word.index(i), end=' ')
    else:
        print("-1", end=' ')