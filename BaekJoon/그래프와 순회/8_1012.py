# 유기농 배추
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque()

    if graph[x][y] == 1:
        graph[x][y] = 0
        q.append((x, y))

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        q.append((nx, ny))

t = int(input())

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

for test_case in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)
