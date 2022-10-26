# 최댓값
import sys
input = sys.stdin.readline

max_num = 0

for i in range(9):
    arr = list(map(int, input().split()))
    for j in range(9):
        if max_num <= arr[j]:
            max_num = arr[j]
            x = i + 1
            y = j + 1

print(max_num)
print(x, y)