# 케빈 베이컨의 6단계 법칙
import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    visited = [0] * (n+1)
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[v] + 1

    return sum(visited)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
count = sys.maxsize
index = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if bfs(i) < count:
        count = bfs(i)
        index = i

print(index)