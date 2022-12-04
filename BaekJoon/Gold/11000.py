# 강의실 배정
import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    s, t = map(int, input().split())
    q.append([s, t])

q.sort()

room = []
heapq.heappush(room, q[0][1])

for i in range(1, n):
    if q[i][0] < room[0]:
        heapq.heappush(room, q[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, q[i][1])

print(len(room))