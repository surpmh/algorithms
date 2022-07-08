# 알고리즘 수업 - 너비 우선 탐색 2
import sys
from collections import deque
input = sys.stdin.readline

def bfs(v, order):
    q.append(v)
    visited[v] = order

    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                order += 1
                visited[i] = order

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
q = deque([])

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort(reverse=True)

bfs(r, 1)

for i in range(1, n+1):
    print(visited[i])