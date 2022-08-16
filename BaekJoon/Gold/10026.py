# 적록색약
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
count1 = 0
count2 = 0

visited = [[False] * (n) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False] * (n) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count2 += 1

print(count1, count2)