# 방 번호
import sys
import math
input = sys.stdin.readline

n = input().rstrip()
num = [0 for _ in range(9)]

for i in n:
     if i == '9':
         num[6] += 1
     else:
         num[int(i)] += 1

num[6] /= 2
num[6] = math.ceil(num[6])

print(max(num))