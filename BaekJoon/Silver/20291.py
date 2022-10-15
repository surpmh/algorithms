# 파일 정리
import sys
input = sys.stdin.readline

n = int(input())
dict = {}

for _ in range(n):
    ext = input().strip().split(".")[1]
    if ext in dict:
        dict[ext] = dict.get(ext) + 1
    else:
        dict[ext] = 1

for i in sorted(dict.items()):
    print(*i)