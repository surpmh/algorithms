# 게임을 만든 동준이
import sys
input = sys.stdin.readline

n = int(input())
level = []
count = 0
for _ in range(n):
    level.append(int(input()))

for i in range(n-1, 0, -1):
    if level[i] <= level[i-1]:
        count += (level[i-1] - level[i] + 1)
        level[i-1] = level[i] -1

print(count)