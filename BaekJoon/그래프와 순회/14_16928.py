# 뱀과 사다리 게임
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([1])
    
    while q:
        x = q.popleft()

        for i in range(1, 7):
            v = x+i

            if board[v] != 0:
                v = board[v]

            if v <= 100 and visited[v] == 0:
                visited[v] = visited[x] + 1
                q.append(v)

                if v == 100:
                    return

n, m = map(int, input().split())
board = [0] * 101
visited = [0] * 101

for _ in range(n+m):
    a, b = map(int ,input().split())
    board[a] = b

bfs()
print(visited[100])