# 두 용액
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
left, right = 0, n-1
result = []
near = sys.maxsize
arr.sort()

while left < right:
    sum = arr[left] + arr[right]

    if abs(sum) < near:
        near = abs(sum)
        result = [arr[left], arr[right]]

    if sum < 0:
        left += 1
    else:
        right -= 1

print(*result)
