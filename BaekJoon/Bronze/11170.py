# 0의 개수
import sys
input = sys.stdin.readline

t = int(input())
for test_case in range(t):
    n, m = map(int, input().split())
    zero = 0

    for i in range(n, m+1):
        zero += str(i).count('0')

    print(zero)