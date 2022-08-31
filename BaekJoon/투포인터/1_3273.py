# 두 수의 합
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
count = 0
left, right = 0, n-1

arr.sort()

while left < right:
    sum = arr[left] + arr[right]
    if sum == x:
        count += 1
    elif sum < x:
        left += 1
        continue
    right -= 1

print(count)