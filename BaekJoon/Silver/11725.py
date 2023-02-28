# 트리의 부모 찾기
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([1])
    vistied[1] = 1

    while q:
        x = q.popleft()
        for i in tree[x]:
            if not vistied[i] and i != 1:
                q.append(i)
                vistied[i] = x

n = int(input())
tree = [[0] for _ in range(n+1)]
vistied = [0] * (n + 1)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

bfs()

for i in range(2, n + 1):
    print(vistied[i])