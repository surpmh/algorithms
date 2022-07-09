# 바이러스
import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    count = 0

    if visited[v] == False:
        q.append(v)
        visited[v] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
                count += 1

    return count

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
q = deque([])

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(bfs(1))