# 버블 소트
import sys
input = sys.stdin.readline

n = int(input())
arr = [[int(input()), i] for i in range(n)]
sorted_arr = sorted(arr)
answer = []

for i in range(n):
    answer.append(sorted_arr[i][1] - arr[i][1])

print(max(answer) + 1)