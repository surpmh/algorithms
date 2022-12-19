# 탑
import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
stack = [[h[0], 1]]
answer = [0]

for i in range(1, n):
    while stack:
        if stack[-1][0] > h[i]:
            answer.append(stack[-1][1])
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([h[i], i+1])

print(*answer)