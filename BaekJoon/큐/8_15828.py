# Router
import sys
from collections import deque
input = sys.stdin.readline

size = int(input())
packets = deque([])

while True:
    n = int(input())

    if n == -1:
        break

    if n == 0:
        packets.popleft()

    if size <= len(packets):
        continue

    if n != 0:
        packets.append(n)

if packets:
    print(*packets)
else:
    print("empty")