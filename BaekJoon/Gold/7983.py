# 압축
import sys
input = sys.stdin.readline

n = int(input())
day = []
off = 1000000000

for _ in range(n):
    d, t = map(int, input().split())
    day.append([d, t])

day.sort(key=lambda x:-x[1])

for d, t in day:
    if t <= off:
        off = t - d
    else:
        off -= d

print(off)