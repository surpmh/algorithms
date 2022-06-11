# 요세푸스 문제 0
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque(range(1, n+1))
result =[]

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())

print("<", end='')
print(*result, sep=', ', end='')
print(">")