# 괄호
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    p = input().rstrip()
    stack = []

    for i in range(len(p)):
        if p[i] == '(':
            stack.append('(')
            
        elif len(stack):
            stack.pop()
        else:
            print("NO")
            break
    else:
        if stack:
            print("NO")
        else:
            print("YES")