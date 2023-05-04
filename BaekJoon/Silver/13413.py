# 오셀로 재배치
import sys
input = sys.stdin.readline

answer = []
result = 0
arr = []

t = int(input())

for _ in range(t):
    n = int(input().rstrip())
    start = list(input().rstrip())
    goal = list(input().rstrip())

    for i in range(n):
        if start[i] != goal[i]:
            arr.append(start[i])

    if arr.count("B") >= arr.count("W"):
        result = arr.count("B")
    else:
        result = arr.count("W")
    answer.append(result)
    arr = []

for answer in answer:
    print(answer)