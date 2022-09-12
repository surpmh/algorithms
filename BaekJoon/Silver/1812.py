# 사탕
import sys
input = sys.stdin.readline

n = int(input())
candy = []
sum = 0

for _ in range(n):
    num = int(input())
    candy.append(num)

    sum += num

sum //= 2

for i in range(n):
    num = 0
    for j in range(1, n, 2):
        num += candy[(i + j) % n]
    print(sum - num)