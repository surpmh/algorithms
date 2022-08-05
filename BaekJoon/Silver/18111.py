# 마인크래프트
import sys
from collections import Counter
input = sys.stdin.readline

n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
dirt = max(map(max, land))
time = sys.maxsize
h = 0

for target in range(dirt+1):
    max_target, min_tartget = 0, 0

    for i in range(n):
        for j in range(m):
            if target < land[i][j]:
                max_target += land[i][j] - target
            else:
                min_tartget += target - land[i][j]

    if max_target + b >= min_tartget:
        if min_tartget + (max_target * 2) <= time:
            time = min_tartget + (max_target * 2)
            h = target

print(time, h)