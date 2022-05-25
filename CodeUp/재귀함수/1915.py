# 피보나치 수열
import sys
input = sys.stdin.readline

def Fibonacci(n):
    if n < 3:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)

num = int(input())

print(Fibonacci(num))