# 풍선 맞추기
import sys
input = sys.stdin.readline

n = int(input())
height = list(map(int, input().split()))
count = [0] * 1000001

for h in height:
    if count[h] == 0:
        count[h-1] += 1
    else:
        count[h] -= 1
        count[h-1] += 1

print(sum(count))