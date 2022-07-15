# 신입 사원
import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(t):
    n = int(input())
    applicant = []
    count = 1

    for _ in range(n):
        s1, s2 = map(int, input().split())
        applicant.append([s1, s2])

    applicant.sort()
    max = applicant[0][1]

    for i in range(1, n):
        if max > applicant[i][1]:
            count += 1
            max = applicant[i][1]

    print(count)