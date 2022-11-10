# 안테나
import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

l.sort()

print(l[(n-1) // 2])