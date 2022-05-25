# 1부터 n까지 합 구하기
import sys
input = sys.stdin.readline

def recursion(n):
    if n < 1:
        return 0
    return n + recursion(n-1)

num = int(input())

print(recursion(num))