# 막대기
import sys
input = sys.stdin.readline

n = int(input())
stick = [int(input()) for _ in range(n)]
stick.reverse()
count = 1
idx = stick[0]

for i in range(1, n):
    if idx < stick[i]:
        count += 1
        idx = stick[i]

print(count)