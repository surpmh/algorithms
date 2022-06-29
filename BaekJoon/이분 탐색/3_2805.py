# 나무 자르기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
height = list(map(int, input().split()))

start = 0
end = max(height)

while start <= end:
    mid = (start + end) // 2
    result = 0

    for i in range(n):
        if height[i] > mid:
            result += height[i] - mid

    if result >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)