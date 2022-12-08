# 꿀 아르바이트
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = list(map(int, input().split()))
p = []

for i in range(1, n):
    t[i] = t[i-1] + t[i]

p.append(t[m-1])

for i in range(m, n):
    p.append(t[i] - t[i-m])

print(max(p))