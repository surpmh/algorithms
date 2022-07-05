# 포도주 시식
import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]
dp = []

if n < 3 :
    dp.append(sum(wine))
else:
    dp.append(wine[0])
    dp.append(wine[0]+wine[1])
    dp.append(max(dp[1], dp[0]+wine[2], wine[1]+wine[2]))

    for i in range(3, n):
        dp.append(max(dp[i-1], dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i]))

print(dp[-1])