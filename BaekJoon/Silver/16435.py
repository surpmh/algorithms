# 스네이크버드
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

for i in h:
    if i <= l:
        l += 1
    else:
        break

print(l)