# 기숙사 바닥
import sys
input = sys.stdin.readline

r, b = map(int, input().split())
len = (r + 4) // 2
tile = r + b

for i in range(1, len):
    if (len-i) * i == tile:
        print(max(i, len-i), min(i, len-i))
        break