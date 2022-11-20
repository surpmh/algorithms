# 한 줄로 서기
import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
answer = [0] * n

for i in range(1, n+1):
    count = 0
    for j in range(n):
        if count == p[i-1] and answer[j] == 0:
            answer[j] = i
            break
        elif answer[j] == 0:
            count += 1

print(*answer)