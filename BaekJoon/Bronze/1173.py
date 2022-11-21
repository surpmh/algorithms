# 운동
import sys
input = sys.stdin.readline

N, m, M, T, R = map(int, input().split())
count = t = 0
X = m

while count < N:
    if m+T > M:
        break
    if X + T <= M:
        X += T
        count += 1
    else:
        X = max(X-R, m)
    t += 1

print(t if count == N else -1)