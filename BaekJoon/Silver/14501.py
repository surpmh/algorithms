# 퇴사
import sys
input = sys.stdin.readline

n = int(input())
time = []
pay = []
dp = []

for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)
    dp.append(p)
dp.append(0)

for i in range(n-1, -1, -1):
    if time[i] + i > n:
        dp[i]= dp[i+1]
    else:
        dp[i] = max(dp[i+1], pay[i] + dp[i + time[i]])

print(dp[0])