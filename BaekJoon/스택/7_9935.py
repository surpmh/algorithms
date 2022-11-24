# 문자열 폭발
import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = list(''.join(input().rstrip()))
stack = []

for s in s1:
    stack.append(s)

    if stack[-len(s2):] == s2:
        del stack[-len(s2):]
    
print(''.join(stack) if stack else "FRULA")