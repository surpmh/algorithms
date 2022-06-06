# 인간-컴퓨터 상호작용
import sys
from collections import Counter
input = sys.stdin.readline

s = input().rstrip()
n = int(input())

for _ in range(n):
    a, l, r = input().rstrip().split()
    l = int(l)
    r = int(r)
    result = 0

    counter = Counter(s[l:r+1])
    for key, value in counter.items():
        if key == a:
            result = value

    print(result)