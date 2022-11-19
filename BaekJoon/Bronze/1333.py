# 부재중 전화
import sys
input = sys.stdin.readline

n, l, d = map(int, input().split())
bell = [0] * (n * l + (n - 1) * 5)

for i in range(n):
    for j in range((l + 5) * i, ((l + 5) * i) + l):
        bell[j] = 1

for i in range(0, len(bell), d):
    if not bell[i]:
        print(i)
        break
else:
    print(i + d)