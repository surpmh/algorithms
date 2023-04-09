# [1차] 뉴스 클러스터링
from collections import Counter

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    a = []
    b = []
    
    for i in range(len(str1) - 1):
        if str1[i:i+2].isalpha():
            a.append(str1[i:i+2])
        
    for i in range(len(str2) - 1):
        if str2[i:i+2].isalpha():
            b.append(str2[i:i+2])

    if len(a) == 0 and len(b) == 0:
        return 65536

    c1 = Counter(a)
    c2 = Counter(b)
    
    com = sum((c1 | c2).values())
    inter = sum((c1 & c2).values())

    return int(inter / com * 65536)

print(solution("FRANCE", "french"))