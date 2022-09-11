# 선물
import sys
input = sys.stdin.readline

n, l, w, h = map(int, input().split())
start, end = 0, max(l, w, h)

for _ in range(100):
    mid = (start+end) / 2
    if (l//mid) * (w//mid) * (h//mid) >= n:
        start = mid
    else:
        end = mid

print('%.10f' %end)