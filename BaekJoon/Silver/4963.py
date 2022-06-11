# 섬의 개수
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x, y):
    if x < 0 or y < 0 or x >= w or y >= h:
        return False

    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x - 1, y - 1)
        dfs(x - 1, y)
        dfs(x - 1, y + 1)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x + 1, y - 1)
        dfs(x + 1, y)
        dfs(x + 1, y + 1)
        return True
    return False
    
while True:
    w, h = map(int, input().split())
    result = 0

    if w + h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if dfs(j, i) == True:
                result += 1

    print(result)