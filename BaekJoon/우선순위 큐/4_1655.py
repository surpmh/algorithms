# 가운데를 말해요
import sys
import heapq
input = sys.stdin.readline

n = int(input())
leftheap =[]
rightheap = []

for _ in range(n):
    x = int(input())

    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -x)
    else:
        heapq.heappush(rightheap, x)

    if rightheap and -leftheap[0] > rightheap[0]:
        min = heapq.heappop(rightheap)
        max = heapq.heappop(leftheap)

        heapq.heappush(leftheap, -min)
        heapq.heappush(rightheap, -max)

    print(-leftheap[0])