# 효율적인 해킹
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    visited = [False] * (n+1)
    count = 1

    q = deque([x])
    visited[x] = True

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                count += 1

    return count

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
max = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

for i in range(1, n+1):
    count = bfs(i)
    
    if max < count:
        max = count
        result = []
        result.append(i)
    elif max == count:
        result.append(i)

print(*result)