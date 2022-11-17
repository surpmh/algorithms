# 그림
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    area = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and draw[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                area += 1

    return area

n, m = map(int, input().split())
draw = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
count = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if draw[i][j] and not visited[i][j]:
            max_area = max(max_area, bfs(i, j))
            count += 1

print(count, max_area, sep="\n")