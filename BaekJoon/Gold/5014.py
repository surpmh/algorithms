# 스타트링크
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    q = deque([x])
    visited[x] = True


    while q:
        x = q.popleft()

        if x == g:
            return floor[x]

        for nx in (x + u, x - d):
            if 0 < nx <= f and not visited[nx]:
                q.append(nx)
                visited[nx] = True
                floor[nx] = floor[x] + 1

    return "use the stairs"

f, s, g, u, d = map(int, input().split())
floor = [0] *  (f + 1)
visited = [False] *  (f + 1)

print(bfs(s))