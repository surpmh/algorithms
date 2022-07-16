# 미로 탐색
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] =  graph[x][y] + 1

    return graph[n-1][m-1]

n, m = map(int, input().split())
graph = [list(map(int, ' '.join(input()).split())) for _ in range(n)]
dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]

print(bfs(0, 0))