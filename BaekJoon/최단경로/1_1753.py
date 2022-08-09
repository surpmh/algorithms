# 최단경로
import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    result[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:

        distance, current = heapq.heappop(heap)

        if result[current] < distance:
            continue

        for n, d in graph[current]:
            next = distance + d
            if next < result[n]:
                result[n] = next
                heapq.heappush(heap, (next, n))


n, m = map(int, input().split())
k = int(input())
INF = sys.maxsize
graph = [[] for _ in range(n + 1)]
result = [INF] * (n + 1)
heap = []

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(k)

for i in range(1, n+1):
    print("INF" if result[i] == INF else result[i])