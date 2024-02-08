#[PCCP 기출문제] 2번 / 석유 시추
from collections import deque

def bfs(land, visited, x, y, result):
    q = deque([[x, y]])
    visited[x][y] = 1

    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    
    min_y = 500
    max_y = 0
    count = 0
    
    while q:
        x, y = q.popleft()
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < len(land) and 0 <= ny < len(land[0]) and visited[nx][ny] == 0 and land[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append([nx, ny])
                
    for i in range(min_y, max_y + 1):
        result[i] += count
    
def solution(land):
    visited = [[0] * len(land[0]) for _ in range(len(land))]
    result = [0] * len(land[0])
    
    for i in range(len(land)):
        for j in range(len(land[0])):
            if visited[i][j] == 0 and land[i][j] == 1:
                bfs(land, visited, i, j, result)
    
    return max(result)

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))