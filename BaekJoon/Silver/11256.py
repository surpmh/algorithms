# 사탕
import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(t):
    j, n = map(int, input().split())

    box = []
    for i in range(n):
        r, c = map(int, input().split())
        box.append(r*c)

    box.sort(reverse=True)
    count = 0
    for b in box:
        j -= b
        count += 1

        if j <= 0:
            print(count)
            break

