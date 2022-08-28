# 스위치 켜고 끄기
import sys
input = sys.stdin.readline

def change(x):
    if status[x] == 0:
        status[x] = 1
    else:
        status[x] = 0
    return

switch = int(input().rstrip())
status = [-1] + list(map(int, input().rstrip().split()))
student = int(input().rstrip())

for _ in range(student):
    g, n = map(int, input().rstrip().split())

    if g == 1:
        for i in range(n, switch+1, n):
            change(i)
    else:
        change(n)
        for i in range(switch//2):
            if n + i > switch or n - i < 1: break
            if status[n-i] == status[n+i]:
                change(n-i)
                change(n+i)
            else:
                break

for i in range(1, switch+1):
    print(status[i], end=' ')

    if i % 20 == 0:
        print()