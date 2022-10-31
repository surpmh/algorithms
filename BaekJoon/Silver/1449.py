# 수리공 항승
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
leak = list(map(int, input().split()))
leak.sort()
count = 1
start = leak[0]
end = leak[0] + l

for i in range(n):
    if start <= leak[i] < end:
        continue
    else:
        start = leak[i]
        end = leak[i] + l
        count += 1

print(count)