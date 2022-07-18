# 2진수 변환
import sys
input = sys.stdin.readline

def binary(n):
    if n // 2:
        binary(n // 2)
    print(n % 2, end='')

n = int(input())
binary(n)