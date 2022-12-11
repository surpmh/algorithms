# 대표 자연수
import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

if (n % 2) == 0:
    print(arr[n // 2 - 1])
else:
    print(arr[n // 2])
