# 전화번호 목록
import sys
input = sys.stdin.readline

def check():
    for i in range(len(tell)-1):
        if tell[i] == tell[i+1][0:len(tell[i])]:
            return print('NO')
    return print('YES')

t = int(input())

for test_case in range(t):
    n = int(input())
    tell = []

    for i in range(n):
        tell.append(input().rstrip())

    tell.sort()

    check()