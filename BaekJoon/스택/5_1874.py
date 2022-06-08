# 스택 수열
import sys
input = sys.stdin.readline

n = int(input())
count = 1
arr = []
stack = []
result = []

for i in range(n):
    num = int(input())
    if num >= count:
        for j in range(count, num+1):
            stack.append(j)
            result.append("+")
        count = num + 1
    elif stack[-1] != num:
        print("NO")
        break
    result.append("-")
    stack.pop()

else:
    print("\n".join(result))