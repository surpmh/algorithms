# 단지번호붙이기
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    house = 0
    q = deque([])
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        house += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == '1' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return house

n = int(input())
graph = [input().rstrip() for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []

dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]

for i in range(n):
        for j in range(n):
            if graph[i][j] == '1' and not visited[i][j]:
                result.append(bfs(i, j))

result.sort()
print(len(result))
for count in result:
    print(count)
