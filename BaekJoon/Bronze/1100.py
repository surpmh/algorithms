# 하얀 칸
import sys
input = sys.stdin.readline

chess = [list(map(str, list(input().strip()))) for _ in range(8)]
count = 0

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if chess[i][j] == 'F':
                count += 1

print(count)