# 보물
import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

a.sort(reverse=True)
b.sort(reverse=False)

print(sum([a[i]*b[i] for i in range(n)]))