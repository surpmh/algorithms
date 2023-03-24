# 안전 영역
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, h):
    q = deque()    
    q.append([x, y])
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > h:
                q.append([nx, ny])
                visited[nx][ny] = True

    return

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
height = set(sum(graph, []))
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
answer = 1

for h in height:
    visited = [[False] * n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visited[i][j]:
                bfs(i, j, h)
                count += 1

            answer = max(answer, count)
        
print(answer)