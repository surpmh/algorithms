# 불!
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while fire:
        x, y = fire.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if miro[nx][ny] != '#' and not visited_f[nx][ny]:
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    fire.append((nx, ny))

    while jihoon:
        x, y = jihoon.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if miro[nx][ny] != '#' and not visited_j[nx][ny]:
                    if not visited_f[nx][ny] or visited_f[nx][ny] > visited_j[x][y] + 1:
                        visited_j[nx][ny] = visited_j[x][y] + 1
                        jihoon.append((nx, ny))

            else:
                return visited_j[x][y]

    return "IMPOSSIBLE"



r, c = map(int, input().split())
miro = []

jihoon = deque()
fire = deque()

visited_j = [[0] * c for _ in range(r)]
visited_f = [[0] * c for _ in range(r)]

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

for _ in range(r):
    miro.append(list(map(str, input().rstrip())))

for i in range(r):
    for j in range(c):
        if miro[i][j] == 'J':
            jihoon.append((i, j))
            visited_j[i][j] = 1
        elif miro[i][j] == 'F':
            fire.append((i, j))
            visited_f[i][j] = 1

print(bfs())