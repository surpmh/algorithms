# 햄버거 분배
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(input().rstrip())
count = 0

for i in range(n):
    if arr[i] == 'P':
        for j in range(i-k, i+k+1):
            if 0 <= j < n and arr[j] == 'H':
                count += 1
                arr[j] = 0
                break

print(count)