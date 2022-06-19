# 수 찾기
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))

for i in range(m):
    start = 0
    end = n-1
    mid = 0
    result = 0

    while start <= end:
        mid = (start + end) // 2
        if a[mid] == b[i]:
            result = 1
            break
        elif a[mid] < b[i]:
            start = mid + 1
        elif a[mid] > b[i]:
            end = mid - 1
    
    print(result)