# 정올 참여 학생 리스트 만들기 1
import sys
input = sys.stdin.readline

n = int(input())
student = []
num_list = []

for _ in range(n):
    code, num, name = input().split()

    if code == 'I':
        if int(num) not in num_list:
            student.append([code, int(num), name])
            num_list.append(int(num))
    elif code == 'D':
        if int(num) in num_list:
            for i in range(len(student)):
                if student[i][1] == int(num):
                    del student[i]
                    break
            num_list.remove(int(num))

student.sort(key=lambda x:x[1])
value = list(map(int, input().split()))

for v in value:
    print(student[v-1][1], student[v-1][2])