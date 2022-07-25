# # 토마토
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if box[nx][ny][nz] == 0:
                    box[nx][ny][nz] = box[x][y][z] + 1
                    q.append((nx, ny, nz))

m, n, h = map(int, input().split())
box = []
result = []
q = deque()
dx = [1, 0, 0, 0, 0, -1] 
dy = [0, -1, 0, 0, 1, 0]
dz = [0, 0, -1, 1, 0, 0]
max_val = 0

for _ in range(h):
    box.append([list(map(int, input().split())) for _ in range(n)])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append((i, j, k))

if all(0 not in j for i in box for j in i):
    print(0)
else:
    bfs()
    if any(0 in j for i in box for j in i):
        print(-1)
    else:
        for i in range(h):
            for j in range(n):
                for k in range(m):
                    max_val = max(max_val, box[i][j][k])
        print(max_val - 1)