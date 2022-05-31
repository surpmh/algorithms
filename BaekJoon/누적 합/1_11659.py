# 구간 합 구하기 4
import sys
sys = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n-1):
    arr[i+1] += arr[i]

arr = [0] + arr

for _ in range(m):
    i, j = map(int, input().split())
    print(arr[j] - arr[i-1])