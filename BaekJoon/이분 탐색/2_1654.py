# 랜선 자르기
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
online = []

for _ in range(k):
    online.append(int(input()))

start = 0
end = sum(online) // n

while start <= end:
    lines = 0
    mid = (start + end) // 2
    if mid == 0:
        mid = 1
    for i in range(k):
        lines += online[i] // mid

    if lines >= n:
        start = mid + 1
    elif lines < n:
        end = mid - 1

print(end)