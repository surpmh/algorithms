# 연속합
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

dp = [num[0]]

for i in range(n-1):
    dp.append(max(num[i+1], dp[i]+num[i+1]))

print(max(dp))