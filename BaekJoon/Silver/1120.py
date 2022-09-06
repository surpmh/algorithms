# 문자열
import sys
input = sys.stdin.readline

a, b = map(str, input().split())
result = sys.maxsize

for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            count += 1

    result = min(result, count)

print(result)