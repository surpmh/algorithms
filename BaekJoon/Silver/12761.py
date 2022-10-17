# 돌다리
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    global count
    q = deque([x])
    visited[x] = True
    visited[x] = 1

    while q:
        x = q.popleft()

        for i in (x+1, x-1, x+a, x-a, x+b, x-b, x*a, x*b):
            if 0 <= i <= 100000 and not visited[i]:
                q.append(i)
                visited[i] = True
                count[i] = count[x] + 1

a, b, n, m = map(int, input().split())
visited = [False] * 100001
count = [0] * 100001

bfs(n)
print(count[m])