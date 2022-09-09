# 나누기
import sys
input = sys.stdin.readline

n = input().rstrip()
f = int(input().rstrip())
temp = int(n[:-2] + '00')

while True:
    if temp % f == 0:
        break
    temp += 1

print(str(temp)[-2:])