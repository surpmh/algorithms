# 연결 요소의 개수
import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque([v])
    visited[v] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    if visited[i] == False:
        bfs(i)
        count += 1

print(count)