# 주유소
import sys
input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))
p = list(map(int, input().split()))

result = p[0] * d[0]
c = p[0]

for i in range(1, n-1):
    if p[i] <= c:
        c = p[i]
        result += c * d[i]
    else:
        result += c * d[i]

print(result)