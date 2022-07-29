# 나이트의 이동
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        if x == x2 and y == y2:
            return graph[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

t = int(input())
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for test_case in range(t):
    n = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    graph = [[0] * n for _ in range(n)]

    print(bfs(x1, y1))