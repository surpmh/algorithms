# 미로 탈출
from collections import deque

def bfs(start, end, maps):
    q = deque()
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    
    for i in range(n):
        if start in maps[i]:
            x = i
            y = maps[i].index(start)
            q.append([x, y])
            break

    while q:
        x, y = q.popleft()
        
        if maps[x][y] == end:
            return visited[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                
    return -1

def solution(maps):
    lever = bfs('S', 'L', maps)
    if lever == -1:
        return -1
    
    exit = bfs('L', 'E', maps)
    if exit == -1:
        return -1
    
    return lever + exit

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))