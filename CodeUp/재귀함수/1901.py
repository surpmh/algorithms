# 1부터 n까지 출력하기
import sys
input = sys.stdin.readline

def recursion(n):
    if n > 1:
        recursion(n-1)

    print(n)

num = int(input())

recursion(num)