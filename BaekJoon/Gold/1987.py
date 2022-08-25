# 알파벳
import sys
input = sys.stdin.readline

def dfs(x, y, count):
    global answer
    answer = max(answer, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and visited[ord(board[nx][ny])-65] == 0:
                visited[ord(board[nx][ny])-65] = 1
                dfs(nx, ny, count + 1)
                visited[ord(board[nx][ny])-65] = 0

    return answer
            

r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
visited = [0]*(26)
visited[ord(board[0][0])-65] = 1
answer = 0

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

print(dfs(0, 0, 1))