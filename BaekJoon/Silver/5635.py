# 생일
import sys
input = sys.stdin.readline

n = int(input())
birth = []
for _ in range(n):
    name, day, month, year = input().rstrip().split()
    birth.append([int(year), int(month), int(day), name])

birth.sort()

print(birth[-1][3])
print(birth[0][3])