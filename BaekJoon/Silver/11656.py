# 접미사 배열
import sys
input = sys.stdin.readline

s = input().rstrip()
arr = []

for i in range(len(s)):
    arr.append(s[i:])

arr.sort()

for i in arr:
    print(i)