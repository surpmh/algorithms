# 피보나치 수열 (Large)
import sys
input = sys.stdin.readline

def Fibonacci(n):
    if n < 3:
        return 1

    if dp[n] == 0:
        dp[n] = Fibonacci(n - 1) + Fibonacci(n - 2)
    return dp[n]

num = int(input())
dp = [0] * 201

print(Fibonacci(num) % 10009)