#스타트와 링크
import sys
inupt = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for i in range(n)]
value = []

#def dfs(i, j):


for i in range(n // 2 - 1):
    for j in range(i+1, n):
        print(i, j)

