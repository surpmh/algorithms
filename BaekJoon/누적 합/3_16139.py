# 인간-컴퓨터 상호작용
import sys
from collections import Counter
input = sys.stdin.readline

# 50점
# s = input().rstrip()
# n = int(input())

# for _ in range(n):
#     a, l, r = input().rstrip().split()
#     l = int(l)
#     r = int(r)
#     result = 0

#     counter = Counter(s[l:r+1])
#     for key, value in counter.items():
#         if key == a:
#             result = value

#     print(result)

# 100점
s = input().rstrip()
n = int(input())
arr = [[0] * 26 for _ in range(len(s))]
arr[0][ord(s[0]) - 97] = 1

for i in range(1, len(s)):
    arr[i][ord(s[i]) - 97] = 1
    for j in range(26):
        arr[i][j] += arr[i - 1][j]

for i in range(n):
    a, l, r = input().split()
    if int(l) > 0:
        result = arr[int(r)][ord(a) - 97] - arr[int(l) - 1][ord(a) - 97]
    else:
        result = arr[int(r)][ord(a) - 97]
    
    print(result)