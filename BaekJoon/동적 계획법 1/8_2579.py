# 계단 오르기
import sys
input = sys.stdin.readline

n = int(input())
step = []
dp = []

for _ in range(n):
    step.append(int(input()))

if n==1:
    print(step[0])
    exit()
elif n == 2:
    print(max(step[0] + step[1], step[1]))
    exit()
    
dp.append(step[0])
dp.append(max(step[0] + step[1], step[1]))
dp.append(max(step[0] + step[2], step[1] + step[2]))

for i in range(3, n):
    dp.append(max(dp[i-2] + step[i], dp[i-3] + step[i] + step[i-1]))

print(dp[-1])
