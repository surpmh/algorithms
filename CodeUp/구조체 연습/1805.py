# 입체기동장치 생산공장
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()

for i in arr:
    print(*i)