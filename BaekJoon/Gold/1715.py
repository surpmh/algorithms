# 카드 정렬하기
import sys
import heapq
input = sys.stdin.readline

t = int(input())
heap = []
sum = 0

for _ in range(t):
    n = int(input())
    heapq.heappush(heap, n)

while len(heap) > 1:
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)

    sum += num1 + num2

    heapq.heappush(heap, num1+num2)

print(sum)