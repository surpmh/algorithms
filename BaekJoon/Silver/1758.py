# 알바생 강호
import sys
input = sys.stdin.readline

n = int(input())
arr = []
sum = 0

for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in range(n):
    tip = arr[i] - i
    if tip < 0:
        continue
    else:
        sum += tip

print(sum)