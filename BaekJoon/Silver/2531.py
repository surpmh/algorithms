# 회전 초밥
import sys
input = sys.stdin.readline
from collections import defaultdict

n, d, k, c = map(int, input().split())
arr = [int(input().strip()) for _ in range(n)]
dish = arr[:k]
count = defaultdict(int)

for i in range(k):
    count[arr[i]] += 1

count[c] += 1
result = len(count)

for i in range(n):
    print(count)
    left = arr[i]
    right = arr[(i+k)%n]

    count[left] -= 1
    count[right] += 1

    if count[left] == 0:
        count.pop(left)

    result = max(result, len(count))

print(result)