# 알고리즘 수업 - 깊이 우선 탐색 1
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(visited, graph, v, order):
    visited[v] = order
    values = graph[v]

    for value in values:
        if visited[value] == 0:
            order = dfs(visited, graph, value, order + 1)
    return order

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(1, m + 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort()

order = 1
dfs(visited, graph, r, order)

for i in range(1, n + 1):
    print(visited[i])