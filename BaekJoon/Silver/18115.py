# 카드 놓기
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
skill = list(map(int, input().split()))
skill.reverse()
answer = deque()

for i in range(n):
    if skill[i] == 1:
        answer.appendleft(i+1)
    elif skill[i] == 2:
        answer.insert(1, i+1)
    elif skill[i] == 3:
        answer.append(i+1)

print(*answer)