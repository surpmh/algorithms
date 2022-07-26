# 집합
import sys
input = sys.stdin.readline

n = int(input())
s = []

for _ in range(n):
    command = input().rstrip().split()
    if len(command) == 2:
        command[1] = int(command[1])

    if command[0] == 'add':
        if command[1] not in s:
            s.append(command[1])
    elif command[0] == 'remove':
        if command[1] in s:
            s.remove(command[1])
    elif command[0] == 'check':
        if command[1] in s:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if command[1] in s:
            s.remove(command[1])
        else:
            s.append(command[1])
    elif command[0] == 'all':
        s = list(range(0, 21))
    elif command[0] == 'empty':
        s = []