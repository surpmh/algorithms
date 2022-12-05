# 컵라면
import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    d, c = map(int, input().split())
    q.append((d, c))

q.sort()
heap = []

for d, c in q:
    heapq.heappush(heap, c)

    if d < len(heap):
        heapq.heappop(heap)
    
print(sum(heap))