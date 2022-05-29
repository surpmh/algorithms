# 회의실 배정
import sys
input = sys.stdin.readline

n = int(input())
time = []
result = 0

for _ in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

time.sort(key=lambda x:x[0])
time.sort(key=lambda x:x[1])

end = 0

for i, j in time:
    if i >= end:
        result += 1
        end = j

print(result)