# 요세푸스 문제
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque(range(1, n+1))

print("<", end="")

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    print(q.popleft(), end="")
    if q:
        print(", ", end="")
    
print(">", end="")