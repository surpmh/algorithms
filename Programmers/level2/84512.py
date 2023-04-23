# 모음사전
from itertools import product

def solution(word):
    words = []

    for i in range(1, 6):
        words.extend(list(map(''.join, product(['A','E','I','O','U'], repeat=i))))
    words.sort()
    
    return words.index(word)+1

print(solution("AAAAE"))