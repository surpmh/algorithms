# 회전하는 큐
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
q = deque(range(1, n+1))
count = 0

for i in range(m):
    if q.index(arr[i]) > (len(q) // 2):
        while q[0] != arr[i]:
            q.appendleft(q.pop())
            count += 1
    else:
        while q[0] != arr[i]:
            q.append(q.popleft())
            count += 1
    
    q.popleft()

print(count)