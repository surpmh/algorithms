# 자료구조는 정말 최고야
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
turn = True

for i in range(m):
    k = int(input())
    stack = list(map(int, input().split()))

    for j in range(1, k):
        if stack[j-1] < stack[j]:
            turn = False

print("Yes" if turn else "No")