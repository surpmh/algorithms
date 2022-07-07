# 알고리즘 수업 - 깊이 우선 탐색 2
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(v, order):
    visited[v] = order

    for i in graph[v]:
        if visited[i] == 0:
            order = dfs(i, order+1)
    return order

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort(reverse=True)

dfs(r, 1)

for i in range(1, n + 1):
    print(visited[i])