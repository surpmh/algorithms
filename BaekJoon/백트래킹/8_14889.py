# 스타트와 링크
import sys
inupt = sys.stdin.readline

def dfs(depth, idx):
    global result

    if depth == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link += graph[i][j]

        result = min(result, abs(start - link))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
result = sys.maxsize

dfs(0, 0)

print(result)