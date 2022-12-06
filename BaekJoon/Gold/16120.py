# PPAP
import sys
input = sys.stdin.readline

string = input().rstrip()
stack = []

for s in string:
    stack.append(s)

    if len(stack) >= 4:
        if stack[-4:] == ['P', 'P', 'A', 'P']:
            for _ in range(4):
                stack.pop()
            stack.append('P')

if stack == ['P', 'P', 'A', 'P'] or stack == ['P']:
    print("PPAP")
else:
    print("NP")