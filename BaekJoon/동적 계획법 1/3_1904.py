# 01타일
import sys
input = sys.stdin.readline

n = int(input())
dp = []

for i in range(n+1):
    if i <= 2:
        dp.append(i)
    else:
        result = (dp[i-2] + dp[i-1]) % 15746
        dp.append(result)

print(dp[n])