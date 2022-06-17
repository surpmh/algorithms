# 알고리즘 수업 - 피보나치 수 1
import sys
input = sys.stdin.readline

def fib(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))

def fibonacci(n):
    global count
    if (n == 1 or n == 2):
        return 1
    f = [0] * n
    f[0], f[1] = 1, 1
    for i in range(2, n):
        count += 1
        f[i] = f[i - 1] + f[i - 2]
    return count

num = int(input())
count = 0

print(fib(num), fibonacci(num))