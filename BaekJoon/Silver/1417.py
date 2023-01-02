# 국회의원 선거
import sys
import heapq
input = sys.stdin.readline

n = int(input())
dasom = int(input())
heap = []
answer = 0

for _ in range(n-1):
    heapq.heappush(heap, -int(input()))

if n == 1:
    print(0)
    exit()

while dasom <= -heap[0]:
    heapq.heappush(heap, heapq.heappop(heap)+1)
    dasom += 1
    answer += 1

print(answer)