# 우박수 (3n+1)
import sys
input = sys.stdin.readline

def func(n):
    print(n)
    if n == 1:
        return n
    if n % 2 != 0:
        func(3 * n + 1)
    else:
        func(n // 2)

n = int(input())
func(n)