# 로또
import sys
input = sys.stdin.readline

def dfs(x):
    if len(lotto) == 6:
        print(*lotto)
        return

    for i in range(x, k+1):
        if s[i] not in lotto:
            lotto.append(s[i])
            dfs(i)
            lotto.pop()

while True:
    s = list(map(int ,input().split()))
    if s == [0]:
        break
    k = s[0]
    lotto = []

    dfs(1)
    print()