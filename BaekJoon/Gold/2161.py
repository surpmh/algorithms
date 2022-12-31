# 카드1
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque([i for i in range(1, n+1)])
answer = []

while len(q) != 1:
    answer.append(q.popleft())
    q.append(q.popleft())

answer.append(q.pop())

print(*answer)