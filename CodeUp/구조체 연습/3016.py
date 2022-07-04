# 1등한 학생의 성적
import sys
input = sys.stdin.readline

n = int(input())
grades = []
for _ in range(n):
    name, score1, score2, score3 = input().split()
    grades.append([name, int(score1), int(score2), int(score3)])

grades.sort(key=lambda x:x[1], reverse=True)

rank2, rank3 = 1, 1

for i in range(1, n):
    if grades[0][2] < grades[i][2]:
        rank2 += 1
    if grades[0][3] < grades[i][3]:
        rank3 += 1

print(grades[0][0], rank2, rank3)