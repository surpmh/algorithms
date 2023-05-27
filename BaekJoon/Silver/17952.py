# 과제는 끝나지 않아!
import sys
input = sys.stdin.readline

t = int(input())
answer = 0
stack = []

for _ in range(t):
    hw = list(map(int, input().split()))

    if hw[0] == 1:
        stack.append([hw[1], hw[2]-1])
    else:
        if stack:
            stack[-1][1] -= 1

    if stack and stack[-1][1] == 0:
        answer += stack[-1][0]
        stack.pop()

print(answer)