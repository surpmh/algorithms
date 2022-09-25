# 나머지 합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split())) + [0]
cnt = [0] * m

for i in range(n):
    arr[i] += arr[i-1]
    cnt[arr[i] % m] += 1

count = cnt[0]

for i in cnt:
    count += i * (i - 1) // 2

print(count)