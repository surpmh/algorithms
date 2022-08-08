# 리모컨
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
if m != 0:
    button = list(map(str, input().split()))
channel = 100
count = abs(channel-n)

if m == 0 or not(set(str(n)) & set(button)):
    count = min(count, len(str(n)))
else:
    for i in range(1000001):
        for j in str(i):
            if j in button:
                break
        else:
            count = min(count, len(str(i)) + abs(i-n))

print(count)