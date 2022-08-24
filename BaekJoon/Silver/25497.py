# 기술 연계마스터 임스
import sys
input = sys.stdin.readline

n = int(input())
tech = input().rstrip()
Rready = []
Kready = []
count = 0

for i in tech:
    if i in str(list(range(1, 10))):
        count += 1
    if i == 'L':
        Rready.append('R')
    if i == 'R':
        if not Rready:
            break
        elif Rready[-1] == 'R':
            Rready.pop()
            count +=1
    if i == 'S':
        Kready.append('K')
    if i == 'K':
        if not Kready:
            break
        elif Kready[-1] == 'K':
            Kready.pop()
            count +=1

print(count)