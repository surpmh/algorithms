# 스케줄 정리
import sys
input = sys.stdin.readline

n = int(input())
schedule = []

for _ in range(n):
    name, year, month, day = input().split()
    schedule.append([name, int(year), int(month), int(day)])

schedule.sort(key=lambda x:(x[1], x[2], x[3], x[0]))

for s in schedule:
    print(s[0])
