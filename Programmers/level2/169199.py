# 리코챗 로봇
from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])
    q = deque()
    visited = [[1000] * m for _ in range(n)]
    
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                q.append([i, j, 0])
                visited[i][j] = 0
    
    while q:
        x, y, count = q.popleft()
        
        if board[x][y] == 'G':
            return count
        
        for i in range(4):
            nx = x
            ny = y
            while 0 <= nx+dx[i] < n and 0 <= ny+dy[i] < m and board[nx+dx[i]][ny+dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]
        
            if visited[nx][ny] > count:
                visited[nx][ny] = count + 1
                q.append([nx, ny, count + 1])
    
    return -1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))