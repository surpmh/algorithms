# 파도반 수열
import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(t):
    dp = [0] * 1001
    n = int(input())

    for i in range(1, n+1):
        if i < 4:
            dp[i] = 1
        elif i < 6:
            dp[i] = 2
        else:
            dp[i] = dp[i-5] + dp[i-1]

    print(dp[n])