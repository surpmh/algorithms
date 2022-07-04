# 성적표 출력
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grades = []

for _ in range(n):
    name, score= input().split()
    grades.append([name, int(score)])

grades.sort(key=lambda x:x[1], reverse=True)

for i in range(m):
    print(grades[i][0])
