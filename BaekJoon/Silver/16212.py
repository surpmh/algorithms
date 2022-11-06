# 정열적인 정렬
import sys
input = sys.stdin.readline

n = input()
a = list(map(int, input().split()))

print(*sorted(a))