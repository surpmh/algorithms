# 성택이의 은밀한 번호
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    passwd = input().rstrip()

    if len(passwd) >= 6 and len(passwd) <= 9:
        print('yes')
    else:
        print('no')