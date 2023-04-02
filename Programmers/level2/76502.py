# 괄호 회전하기
from collections import deque

def is_parenthesis(s):
    stack = [s[0]]

    for i in range(1, len(s)):
        if stack and s[i] == ')' and stack[-1] == '(':
            stack.pop()
        elif stack and s[i] == ']' and stack[-1] == '[':
            stack.pop()
        elif stack and s[i] == '}' and stack[-1] == '{':
            stack.pop()
        else:
            stack.append(s[i])

    if stack:
        return False
    else:
        return True

def solution(s):
    answer = 0
    s = deque(s)

    if len(s) == 0:
        return 0

    for _ in range(len(s)-1):
        if is_parenthesis(s):
            answer += 1
        
        s.append(s.popleft())

    return answer

print(solution("[](){}"))