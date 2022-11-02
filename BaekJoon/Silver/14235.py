# 크리스마스 선물
import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    a = input().rstrip()

    if a == '0':
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(-1)
    else:
        a = list(map(int, a.split()))
        for i in range(1, a[0]+1):
            heapq.heappush(heap, -a[i])