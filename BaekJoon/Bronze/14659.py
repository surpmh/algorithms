# 한조서열정리하고옴ㅋㅋ
import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))

enemy = 0

for i in range(n):
    count = 0
    for j in range(i+1, n):
        if h[i] >= h[j]:
            count += 1
        else:
            break
    enemy = max(enemy, count)

print(enemy)