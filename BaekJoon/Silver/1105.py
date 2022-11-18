# 팔
import sys
input = sys.stdin.readline

l, r = map(str, input().rstrip().split())
count = 0

if len(l) != len(r):
    print(0)
else:
    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] == '8':
                count += 1
        else:
            break

    print(count)