# 1, 2, 3 더하기
import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(t):
    dp = [0, 1, 2, 4]

    n = int(input())

    if n >= len(dp):
        for i in range(len(dp), n+1):
            dp.append(dp[i-3]+dp[i-2]+dp[i-1])

    print(dp[n])