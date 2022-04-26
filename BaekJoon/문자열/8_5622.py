dial = ['ABC', 'DEF', 'GHI','JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sum = 0
word = input()

for i in range(len(word)):
    time = 0
    for j in range(8):
        if word[i] in dial[j]:
            time += (j + 3)
        else:
            continue
        sum += time

print(sum)