# 암호 만들기
import sys
input = sys.stdin.readline

def dfs():
    if len(word) == l:
        vo = 0
        co = 0
        for i in word:
            if i in 'aeiou':
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print(''.join(map(str, word)))
        return
    else:
        for s in alphabet:
            if s in word or word and word[-1] > s:
                continue
            else:
                word.append(s)
                dfs()
                word.pop()

l, c = map(int, input().split())
word = []

alphabet = input().rstrip().split()
alphabet.sort()

dfs()