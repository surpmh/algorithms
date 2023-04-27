# 무인도 여행
from collections import deque

def bfs(maps, visited, x, y):
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    visited[x][y] = 1
    q = deque([(x, y)])
    sum = int(maps[x][y])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if not visited[nx][ny] and maps[nx][ny] != "X":
                    sum += int(maps[nx][ny])
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    return sum

def solution(maps):
    answer = []
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j] and maps[i][j] != "X":
                answer.append(bfs(maps, visited, i, j))
                visited[i][j] = 1

    if answer:
        return sorted(answer)
    else:
        return [-1]

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))