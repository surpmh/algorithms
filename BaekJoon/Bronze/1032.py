# 명령 프롬프트
import sys
input = sys.stdin.readline

n = int(input())
a = list(input().rstrip())

for _ in range(n-1):
    b = list(input().rstrip())
    for i in range(len(a)):
        if a[i] != b[i]:
            a[i] = '?'

print(''.join(a))