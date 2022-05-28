# 동전 0
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
result = 0
for _ in range(n):
    coin.append(int(input()))

coin.reverse()

for i in range(n):
    if k // coin[i] != 0:
        result += k // coin[i]
        k -= coin[i] * (k // coin[i])
    else:
        continue

print(result)