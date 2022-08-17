# IOIOI
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()
count = 0
result = 0
i = 1

while i < m-1:
    if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == 'I':
        count += 1
        if count == n:
            count -= 1
            result += 1
        i += 1
    else:
        count = 0
    i += 1

print(result)