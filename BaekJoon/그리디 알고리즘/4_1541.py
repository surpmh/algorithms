# 잃어버린 괄호
import sys
input = sys.stdin.readline

n = list(map(str, input().rstrip().split('-')))
value = []

for i in n:
    i = i.split('+')
    i = list(map(int, i))
    value.append(sum(i))

for i in range(1, len(value)):
    value[i] = -value[i]

print(sum(value))
