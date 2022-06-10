# 카드2
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque([_ for _ in range(1, n+1)])

while len(q) != 1:
    q.popleft()
    q.append(q[0])
    q.popleft()

print(*q)