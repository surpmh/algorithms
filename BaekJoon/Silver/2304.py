# 창고 다각형
import sys
input = sys.stdin.readline

t = int(input())
coordinates = []
h = 0
w = 0
h_idx = 0
answer = 0
arr = [0] * 10001

for _ in range(t):
    x, y = map(int, input().split())
    arr[x] = y

    if h < y:
        h = y
        h_idx = x

    w = max(w, x)

curr = 0
for i in range(h_idx + 1):
    curr = max(curr, arr[i])
    answer += curr

curr = 0
for i in range(w, h_idx, -1):
    curr = max(curr, arr[i])
    answer += curr

print(answer)