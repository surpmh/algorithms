# 철벽 보안 알고리즘
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = []
    rule  = []

    for _ in range(3):
        s.append(input().rstrip().split())

    for i in s[0]:
        rule.append(s[1].index(i))

    print(' '.join(s[2][i] for i in rule))