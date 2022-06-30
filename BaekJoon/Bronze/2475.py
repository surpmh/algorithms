# 검증수
import sys
import math
input = sys.stdin.readline

num = list(map(int, input().split()))
result = 0

for n in num:
    result += math.pow(n, 2)

print(int(result % 10))