import sys

word = input().upper()
word_list = list(set(word))
max = 0

for i in range(len(word_list)):
    if max < word.count(word_list[i]):
        max = word.count(word_list[i])
        index = i
        egtikeul = False
    elif max == word.count(word_list[i]) and word_list[index] != word_list[i]:
        egtikeul = True

if egtikeul == False:
    print(word_list[index])
else:
    print("?")