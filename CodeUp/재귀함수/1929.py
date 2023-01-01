# 우박수 (3n+1) (reverse)
import sys
input = sys.stdin.readline

def func(n):
    if n == 1:
        return print(n)
    if n % 2 != 0:
        func(3 * n + 1)
    else:
        func(n // 2)
    return print(n)

n = int(input())
func(n)