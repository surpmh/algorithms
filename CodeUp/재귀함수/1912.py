# 팩토리얼 계산
import sys
input = sys.stdin.readline

def factorial(n):
    if n < 1:
        return 1
    return factorial(n - 1) * n

num = int(input())

print(factorial(num))