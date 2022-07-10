# DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline

def dfs(v):
    dfs_visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if dfs_visited[i] == False:
            dfs(i)
    
    return

def bfs(v):
    q = deque([])
    q.append(v)
    bfs_visited[v] = True

    while q:
        v = q[0]
        print(q.popleft(), end=' ')
        for i in graph[v]:
            if bfs_visited[i] == False:
                q.append(i)
                bfs_visited[i] = True


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for g in graph:
    g.sort()

dfs(v)
print()
bfs(v)
