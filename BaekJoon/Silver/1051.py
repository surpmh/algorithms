# 숫자 정사각형
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rectangle = [input() for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        for k in range(min(n, m)):
            if i + k < n and j + k < m and rectangle[i][j] == rectangle[i+k][j] == rectangle[i][j+k] == rectangle[i+k][j+k]:
                answer = max(answer, (k+1)**2)

print(answer)