# 에너지 모으기
import sys
input = sys.stdin.readline

def dfs(x):
    global answer
    if len(w) == 2:
        answer = max(answer, x)
        return answer
    
    for i in range(1, len(w)-1):
        e = w[i-1] * w[i+1]
        v = w.pop(i)
        dfs(x + e)
        w.insert(i, v)

n = int(input())
w = list(map(int, input().split()))
answer = 0

dfs(0)
print(answer)