# 토마토
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if box[nx][ny] == 0:
                    box[nx][ny] = box[x][y] + 1
                    q.append((nx, ny))

n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(m)]
q = deque()
dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]

if all(0 not in _ for _ in box):
    print(0)
else:
    for i in range(m):
        for j in range(n):
            if box[i][j] == 1:
                q.append((i, j))

    bfs()

    if any(0 in _ for _ in box):
        print(-1)
    else:
        print(max(map(max, box)) - 1)