# 통나무 건너뛰기
import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(t):
    result = 0
    n = int(input())
    log = list(map(int, input().split()))

    log.sort()

    for i in range(n-2):
        result = max(result, abs(log[i] - log[i+2]))

    print(result)