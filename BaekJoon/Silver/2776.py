# 암기왕
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr1 = set(map(int, input().split()))

    n = int(input())
    arr2 = list(map(int, input().split()))

    for num in arr2:
        print("1" if num in arr1 else "0")