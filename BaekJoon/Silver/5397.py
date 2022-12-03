# 키로거
import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(t):
    l = input().rstrip()
    left = []
    right = []

    for i in l:
        if i == ">":
            if right:
                left.append(right.pop()) 
        elif i=="<":
            if left:
                right.append(left.pop())
        elif i=="-":
            if left:
                left.pop()
        else:
            left.append(i)

    left.extend(reversed(right))
    print("".join(left))