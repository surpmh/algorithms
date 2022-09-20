# 센서
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensors = sorted(list(map(int, input().split())))

d = []
for i in range(1, n):
    d.append(sensors[i] - sensors[i-1])

d.sort()

print(sum(d[:(n-k)]))