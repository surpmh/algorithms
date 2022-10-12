# 눈덩이 굴리기
import sys
input = sys.stdin.readline

def dfs(idx, time, size):
    global answer
    if m < time:
        return
    else:
        answer = max(answer, size)

    if idx <= n - 1:
        dfs(idx+1, time+1, size+snowball[idx+1])
    if idx <= n - 2:
        dfs(idx+2, time+1, size//2+snowball[idx+2])

n, m = map(int, input().split())
snowball = [0] + list(map(int, input().split()))
answer = 0

dfs(0, 0, 1)

print(answer)