# 수들의 합
import sys
input = sys.stdin.readline

n = int(input())
count = 0
sum = 0
num = 1

while True:
    sum += num
    num += 1
    count += 1

    if sum == n:
        print(count)
        break
    elif sum > n:
        print(count - 1)
        break