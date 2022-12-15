# 점프 점프
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [n + 1] * (n + 1)
dp[0] = 0

for i in range(n):
    for j in range(a[i]):
        if i + j < n:
            dp[i + j + 1] = min(dp[i + j + 1], dp[i] + 1)

print(dp[n - 1] if dp[n - 1] < n + 1 else -1)