import sys

count = 0

N = int(input())

for i in range(N):
    word = sys.stdin.readline()
    set_list = set()

    for j in range(1, len(word)):
        if word[j] == word[j-1]:
            continue
        else:
            if word[j-1] in set_list:
                count += 1
                break
            set_list.add(word[j-1])

print(N - count)