# 회장뽑기
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    visited = [-1] * (n+1)
    q = deque([x])
    visited[x] = 0

    while q:
        x = q.popleft()

        for v in member[x]:
            if visited[v] == -1:
                visited[v] = visited[x] + 1
                q.append(v)

    return max(visited)

n = int(input())
member = [[0] for i in range(n+1)]
score = sys.maxsize

while True:
    a, b = map(int, input().split())

    if a == -1 and b == -1:
        break

    member[a].append(b)
    member[b].append(a)

for i in range(1, n+1):
    if score > bfs(i):
        score = bfs(i)
        candidate = []
        candidate.append(i)

    elif score == bfs(i):
        candidate.append(i)

print(score, len(candidate))
print(*candidate)