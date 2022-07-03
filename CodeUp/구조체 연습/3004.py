# 데이터 재정렬
import sys
input = sys.stdin.readline

def binary_sort(value):
    start = 0
    end = n

    while start <= end:
        mid = (start + end) // 2

        if value == sort[mid]:
            return mid
        if value < sort[mid]:
            end = mid - 1
        else:
            start = mid + 1

n = int(input())
arr = list(map(int, input().split()))

sort = sorted(arr)

for i in arr:
    print(binary_sort(i), end=' ')