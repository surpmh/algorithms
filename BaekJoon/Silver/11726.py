# 2×n 타일링
import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1, 2]

if n > 2:
    for i in range(3, n+1):
        dp.append(dp[i-2] + dp[i-1])

print(dp[n] % 10007)