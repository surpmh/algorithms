# 최고의 피자
import sys
import math
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
c = int(input())
d = []

price = c / a

for _ in range(n):
    d.append(int(input()))

d.sort(reverse=True)

for i in range(n):
    c += d[i]

    if price < (c / (a + b * (i+1))):
        price = (c / (a + b * (i+1)))
    else:
        break

print(math.floor(price))