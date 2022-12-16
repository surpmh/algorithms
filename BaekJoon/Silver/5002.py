# 도어맨
import sys
from collections import deque
input = sys.stdin.readline

x = int(input())
line = deque(list(input().rstrip()))
wait = []
m = 0
w = 0

while line:
    if wait:
        gender = wait.pop()
        if gender == 'M':
            m += 1
        else:
            w += 1
    else:
        gender = line[0]

        if gender == 'M':
            if abs((m + 1) - w) <= x:
                line.popleft()
                m += 1
            elif len(line) > 2 and line[1] == 'W':
                wait.append(line.popleft())
                line.popleft()
                w += 1
            else:
                break
        else:
            if abs((w + 1) - m) <= x:
                line.popleft()
                w += 1
            elif len(line) > 2 and line[1] == 'M':
                wait.append(line.popleft())
                line.popleft()
                m += 1
            else:
                break

print(m+w)