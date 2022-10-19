# ABCDE
import sys
input = sys.stdin.readline

def dfs(idx, depth):
    global ans
    if depth == 4:
        ans = 1
        return
    for i in graph[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth+1)
            visited[i] = False

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n
ans = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

if ans:
    print(1)
else:
    print(0)