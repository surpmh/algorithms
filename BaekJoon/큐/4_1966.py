# 프린터 큐
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    s = deque(list(map(int, input().split())))
    index = deque(range(n))
    count = 0

    for i in range(n):
        while max(s) != s[0]:
            s.append(s.popleft())
            index.append(index.popleft())
        count += 1
        if index[0] == m:
            break
        s.popleft()
        index.popleft()

    print(count)
        
