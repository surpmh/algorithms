# 게임 맵 최단거리
from collections import deque

def bfs(maps):
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    n = len(maps[0])
    m = len(maps)
    visited = [[0] * n for _ in range(m)]
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and maps[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    return visited[m-1][n-1]

def solution(maps):
    answer = bfs(maps)

    return answer if answer else -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))