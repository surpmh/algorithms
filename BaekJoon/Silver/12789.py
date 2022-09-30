# 도키도키 간식드리미
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
line = deque(list(map(int, input().split())))
turn = 1
stack = []

while line:
    if line[0] == turn:
        line.popleft()
        turn += 1
    elif stack and stack[-1] == turn:
        stack.pop()
        turn += 1
    else:
        stack.append(line.popleft())

while stack:
    if stack[-1] == turn:
        stack.pop()
        turn += 1
    else:
        break

print("Nice" if not stack else "Sad")
