# 우체국
import sys
input = sys.stdin.readline

n = int(input())
village = []
answer = 0
sum = 0
l = 0

for i in range(n):
    x, a = map(int, input().split())
    village.append((x, a))
    sum += a

village.sort(key=lambda x:x[0])

for v in village:
    l += v[1]
    if l >= sum/2:
        print(v[0])
        break