# 계란으로 계란치기
import sys
input = sys.stdin.readline

def dfs(idx):
    global answer

    if idx == n:
        count = 0
        for e in egg:
            if e[0] <= 0:
                count += 1
            answer = max(answer, count)
        return
    if egg[idx][0] <= 0:
        dfs(idx + 1)
    else:
        broken = True
        for i in range(n):
            if i != idx and egg[i][0] > 0:
                broken = False
                egg[idx][0] -= egg[i][-1]
                egg[i][0] -= egg[idx][-1]
                dfs(idx + 1)
                egg[idx][0] += egg[i][-1]
                egg[i][0] += egg[idx][-1]
        if broken:
            dfs(n)

n = int(input())
answer = 0
egg = []
[egg.append(list(map(int, input().split()))) for _ in range(n)]

dfs(0)
print(answer)