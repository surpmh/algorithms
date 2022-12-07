# 아이들과 선물 상자
import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
box = []
for i in list(map(int, input().split())):
    heapq.heappush(box, -i)
children = list(map(int, input().split()))

for c in children:
    gift = -heapq.heappop(box)

    if gift < c:
        print(0)
        exit()

    if gift - c > 0:
        heapq.heappush(box, -(gift - c))

print(1)