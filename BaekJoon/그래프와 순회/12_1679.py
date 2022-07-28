# 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(n)

    while q:    
        x = q.popleft()
        if x == k:
            return dist[x]

        for i in (x-1, x+1, x*2):
            if 0 <= i <= max and not dist[i]:
                dist[i] = dist[x]+1
                q.append(i)

n, k = map(int, input().split())
max = 100000
dist = [0] * (max+1)

print(bfs())