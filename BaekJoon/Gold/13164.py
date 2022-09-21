# 행복 유치원
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kids = list(map(int, input().split()))
arr = []

for i in range(1, n):
    arr.append(kids[i] - kids[i-1])

arr.sort(reverse=True)
print(sum(arr[k-1:]))