# 부분합
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, 0
sub = 0
length = sys.maxsize

if sum(arr) < s:
    print(0)
else:
    while True:
        if sub >= s:
            length = min(length, right - left)
            sub -= arr[left]
            left += 1
        elif right == n:
            break
        else:
            sub += arr[right]
            right += 1

    print(length)