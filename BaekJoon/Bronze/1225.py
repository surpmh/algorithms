# 이상한 곱셈
import sys
input = sys.stdin.readline

a, b = map(str, input().split())

a = list(map(int, a))
b = list(map(int, b))

print(sum(a)*sum(b))