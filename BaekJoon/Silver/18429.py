# 근손실
import sys
input = sys.stdin.readline

def dfs(c, w):
    global count

    if w < 500:
        return

    if c == n:
        count += 1

    for i in range(n):
        if check[i] == 0:
            check[i] = 1
            dfs(c+1, w + kit[i] - m)
            check[i] = 0

n, m = map(int, input().split())
kit = list(map(int, input().split()))
check = [0] * n
count = 0

dfs(0, 500)

print(count)